#!/usr/bin/env python3
"""Disk Monitor - monitors disk usage and sends alerts when thresholds exceeded."""
import psutil, argparse, time, logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def check_disks(threshold=80):
      alerts = []
      for p in psutil.disk_partitions():
                try:
                              u = psutil.disk_usage(p.mountpoint)
                              if u.percent >= threshold:
                                                alerts.append({"mount": p.mountpoint, "percent": u.percent, "free_gb": round(u.free/(1024**3),2)})
                                                logging.warning(f"{p.mountpoint} is {u.percent}% full")
                                        except: pass
                                              return alerts

if __name__ == "__main__":
      parser = argparse.ArgumentParser()
    parser.add_argument("--threshold", type=int, default=80)
    args = parser.parse_args()
    alerts = check_disks(args.threshold)
    if not alerts: print("All disks OK")
      
