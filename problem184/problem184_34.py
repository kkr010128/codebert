import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
S = readline().decode().rstrip()
if S[2] == S[3] and S[4] == S[5]:
    print('Yes')
else:
    print('No')