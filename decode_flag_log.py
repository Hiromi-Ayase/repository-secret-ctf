#!/usr/bin/env python3
import base64
import sys


line = sys.stdin.readline().strip()
value = line.split("=", 1)[1]
print(base64.b64decode(value[::-1]).decode())
