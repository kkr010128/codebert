import sys
import re

stri = sys.stdin.readline()
ret = re.match( '^(hi)+$', stri)
if ret:
	print("Yes")
else:
	print("No")
sys.stdout.flush()