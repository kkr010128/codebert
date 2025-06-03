import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
SS = ['SUN','MON','TUE','WED','THU','FRI','SAT']
S = readline().decode().rstrip()
for i in range(7):
    if S == SS[i]:
        print(7-i)
        sys.exit()