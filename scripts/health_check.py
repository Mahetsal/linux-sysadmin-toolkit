#!/usr/bin/env python3
"""System Health Check - generates comprehensive system resource report."""
import platform, psutil, socket, json, argparse
from datetime import datetime

def get_cpu_info():
      return {"cores": psutil.cpu_count(), "usage": psutil.cpu_percent(interval=1)}

def get_memory_info():
      mem = psutil.virtual_memory()
      return {"total_gb": round(mem.total/(1024**3),2), "used_gb": round(mem.used/(1024**3),2), "percent": mem.percent}

def get_disk_info():
      disks = []
      for p in psutil.disk_partitions():
                try:
                              u = psutil.disk_usage(p.mountpoint)
                              disks.append({"mount": p.mountpoint, "total_gb": round(u.total/(1024**3),2), "percent": u.percent, "status": "CRITICAL" if u.percent>90 else "OK"})
                          except: pass
                                return disks

def generate_report():
      return {"timestamp": datetime.utcnow().isoformat(), "system": {"hostname": platform.node(), "os": platform.system()}, "cpu": get_cpu_info(), "memory": get_memory_info(), "disks": get_disk_info()}

if __name__ == "__main__":
      report = generate_report()
      print(json.dumps(report, indent=2))
  
