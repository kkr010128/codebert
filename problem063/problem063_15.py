import sys
s=sys.stdin.read().lower()
[print(chr(i),':',s.count(chr(i)))for i in range(97,123)]