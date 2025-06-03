import sys

w = sys.stdin.readline().strip().lower()

cnt = 0
while True:
    line = sys.stdin.readline().strip()
    if line == 'END_OF_TEXT':
        break
        
    words = line.split(' ')
    for i in words:
        if i.lower() == w:
            cnt += 1

print(cnt)