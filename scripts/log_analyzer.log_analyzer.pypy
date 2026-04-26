#!/usr/bin/env python3
"""Log Analyzer - parses system logs for errors, warnings, and failed logins."""
import re, os, argparse
from collections import Counter

def analyze_log(filepath):
      errors, warnings, failed = [], [], []
      with open(filepath, "r", errors="ignore") as f:
                for line in f:
                              low = line.lower()
                              if any(k in low for k in ["error","fail","critical"]): errors.append(line.strip())
                                            if any(k in low for k in ["warn","timeout"]): warnings.append(line.strip())
                                                          if "failed password" in low:
                                                                            ip = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
                                                                            failed.append(ip.group(1) if ip else "unknown")
                                                                return {"errors": len(errors), "warnings": len(warnings), "failed_logins": len(failed), "top_ips": dict(Counter(failed).most_common(5))}

        if __name__ == "__main__":
              parser = argparse.ArgumentParser()
              parser.add_argument("--log", required=True)
              args = parser.parse_args()
              print(analyze_log(args.log))
          
