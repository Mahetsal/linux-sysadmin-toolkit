# Linux Sysadmin Toolkit

Python and Bash scripts for Linux system administration - health checks, log analysis, disk monitoring, and automated backups.

## Features

- System Health Check - CPU, memory, disk, network status at a glance
- - Log Analyzer - Parse and summarize syslog, auth, and application logs
  - - Disk Monitor - Track disk usage with configurable alerts
    - - Automated Backups - Scheduled backup with rotation and compression
     
      - ## Quick Start
     
      - ```bash
        git clone https://github.com/Mahetsal/linux-sysadmin-toolkit.git
        cd linux-sysadmin-toolkit
        pip install -r requirements.txt
        python scripts/health_check.py
        ```

        ## Tech Stack

        - Python 3.11+
        - - Bash 5.0+
          - - psutil for system metrics
            - - Compatible with Ubuntu, CentOS, Debian
             
              - ## License
             
              - MIT License
              - 
