# Description

The Zscaler Internet Access (ZIA) audit report script uses Zscaler's Cloud Service API to download an audit log report 
for a specified timeframe and saves the response in CSV format. With the `-5` or `-24` flag, the script will create an 
audit log report for the 5 minutes or 24 hours previous to script execution. 
Moreover, the script can also send audit scripts to a sys log server specified.

> It is recommended to retrieve the API key, username, and password from a password management system via API.

---
# Run Locally
```bash
# Clone repo
git clone https://github.com/sergitopereira/zscaler_audit_logs.git

# Install dependencies
pip3 install -r zscaler_audit_logs/requirements.txt

# Usage
python3 zscaler_audit_logs -h
```

# Run in a Virtual Environment
```bash
# Clone repo
git clone https://github.com/sergitopereira/zscaler_audit_logs.git

# Create and enter virtual environment
python3 -m venv zscaler_audit_logs/venv
source zscaler_audit_logs/venv/bin/activate

# Install dependencies
pip install -r zscaler_audit_logs/requirements.txt

# Usage
python zscaler_audit_logs -h
```
# Run with Docker

```bash
# Download Dockerfile
wget https://raw.githubusercontent.com/sergitopereira/zscaler_audit_logs/master/Dockerfile

# Build Image and Run Container
docker build -t audit .  
docker run -it audit bash

# Usage (program is in /app/)
python app -h
```
# Usage

```
usage: zscaler_audit_logs [-h] [-24] [-5] -a API_KEY -u USER -p PASSWORD -c CLOUD [-v] [-rlog REMOTE_LOGGING]

optional arguments:
  -h, --help            show this help message and exit
  -24, --last-24        Get audit report for last 24 hours (1440 min) and save result in csv file
  -5, --last-5          Get audit report for last 5 minutes and save result in csv file
  -a API_KEY, --api_key API_KEY
                        ZIA API key
  -u USER, --user USER  ZIA username (email address)
  -p PASSWORD, --password PASSWORD
                        ZIA password
  -c CLOUD, --cloud CLOUD
                        ZIA cloud
  -v, --version         show the version information and exit
  -rlog REMOTE_LOGGING, --remote_logging REMOTE_LOGGING
                        Remote syslog server information. Format IP address:protocol:port Example X.X.X.X:PROTOCOL:PORT or FQDN:PROTOCOL:PORT
```
---

# Credits
```
Sergio Pereira 
Zscaler Professional Services
```
