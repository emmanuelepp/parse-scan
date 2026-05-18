#!/usr/bin/env python3
import re, sys
from pathlib import Path

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <scan_file>", file=sys.stderr)
    sys.exit(1)

path = Path(sys.argv[1])
if not path.is_file():
    print(f"Error: file not found: {path}", file=sys.stderr)
    sys.exit(1)

pattern = r'(\d+)/(?:tcp\s+open|udp\s+open|open)\b'
ports = re.findall(pattern, path.read_text())

if not ports:
    print("No open ports found.", file=sys.stderr)
    sys.exit(1)

print(','.join(sorted(set(ports), key=int)))