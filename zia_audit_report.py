import pdb

from helpers.zia_api_calls import ZsTalker
import time
from datetime import datetime
from helpers.remote_syslog import SendLogs


def check_report_status(zs):
    """
    Function to check the status of the report.
    :param zs: instance of zsTalker
    return boolean
    """
    count = 0
    complete = False
    while (complete == False and count < 4):
        response = zs.list_auditlogEntryReport()
        if "complete" in response.get('status').lower():
            complete = True
        else:
            count = count + 1
            time.sleep(3)
    if not complete:
        raise ValueError("Was not possible to generate the report")
    return complete


def write_csv(csv_report):
    """
    Function to write to csv file
    :param csv_report:
    :return: none
    """
    date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
    with open(f'audit_{date}.csv', 'bw') as f:
        f.write(csv_report)
    return


def get_audit_report(api_key, user, password, cloud, start_time, end_time=None, rlog=None):
    """
    Main function to obtain audit reports
    :param api_key: type string. API key
    :param user: type string. User
    :param password: type string. Password
    :param cloud: type string. Zscaler cloud
    :param start_time: time in minutes
    :param end_time: time in minutes
    :param rlog:  type string. Remove sys log server info: IP:PROTOCOL:PORT
    :return: none
    """
    if start_time:
        endtime = time.time()
        start = endtime - (start_time * 60)

    else:
        print('convert')

    zs = ZsTalker(f'zsapi.{cloud}')
    zs.authenticate(api_key, user, password)
    zs.add_auditlogEntryReport(startTime=start * 1000, endTime=endtime * 1000)
    check_report_status(zs)
    report = zs.download_auditlogEntryReport()
    write_csv(report.content)
    j = report.content.decode('UTF-8').split('\n')
    if rlog:
        rlog = rlog.split(':')
        if rlog[1].lower() not in ['tcp', 'udp']:
            raise ValueError("Invalid remote sys log protocol")
        rlog = SendLogs(ip=rlog[0], port=rlog[2], protocol=rlog[1])
        for i in j:
            rlog.send_logs(i)
