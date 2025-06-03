import sys
w = input().lower()
lines = sys.stdin.read()
line=lines[0:lines.find('END_OF_TEXT')].lower().split()
print(line.count(w))