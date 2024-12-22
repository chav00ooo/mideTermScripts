# Vulnerability Scanner

## Project Objectives:
The Vulnerability Scanner is a Python-based tool designed to automate the process of identifying open ports, detecting services running on them, and cross-referencing those services with known vulnerabilities. This project demonstrates the use of Python for security automation, specifically targeting authorized systems like "localhost" and "scanme.nmap.org".

## Features:
- Scans specified targets for open ports within a given range.
- Detects services running on open ports using Nmap.
- Matches services and ports to known vulnerabilities using a JSON database.
- Generates detailed vulnerability reports in CSV format for further analysis.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher.
- Required libraries: `python-nmap`, `json`, `csv`.
- Ensure you have permission to scan the targets.

### Running the Scanner
1. Configure the targets and port range in the `vulnerabilityScanner.py` file:
   ```python
   TARGETS = ["127.0.0.1", "scanme.nmap.org"]
   PORT_RANGE = range(0, 1025)
   ```
2. Ensure the `vulnerability_db.json` file exists in the same directory and contains up-to-date vulnerabilities. Example:
   ```json
   }
    "22": ["CVE-2020-15778: SSH command injection vulnerability"],
    "80": ["CVE-2021-44228: Log4j vulnerability in HTTP servers"],
    "443": ["CVE-2022-0778: OpenSSL infinite loop vulnerability"],
    "631": ["CVE-2018-20673: IPP printing service remote denial of service"],
    "ssh": ["CVE-2016-20012: Weak SSH key exchange"],
    "http": ["CVE-2021-3129: Laravel debug mode vulnerability"],
    "https": ["CVE-2019-11043: PHP-FPM remote code execution"],
    "ipp": ["CVE-2018-20673: IPP printing service remote denial of service"],
    "apache": ["CVE-2021-41773: Apache path traversal vulnerability"]
   }
   ```
3. Run the scanner:
   
   python vulnerabilityScanner.py
  
4. View results in the console or the generated `vulnerability_report.csv` file.

## Output
- **Console Output**: Displays open ports, detected services, and associated vulnerabilities.
- **CSV Report**: A file named `vulnerability_report.csv` is created, containing detailed results.

### Example CSV Output
```
Target,Port,Service,Version,Vulnerabilities
127.0.0.1,631,ipp,2.3,CVE-2018-20673: IPP printing service remote denial of service
scanme.nmap.org,22,ssh,OpenSSH 6.6,CVE-2020-15778: SSH command injection vulnerability
```

## Dependencies
- `python-nmap`: For service detection and integration with Nmap.
- `json`: For handling the vulnerability database.
- `csv`: For generating structured reports.

To install dependencies manually:
```bash
pip install python-nmap
```

## Additional Information
- Only scan systems you own or are authorized to scan.
- Ensure the `vulnerability_db.json` file is updated regularly with the latest CVEs.
- Reduce the port range or timeout for quicker scans if needed.

