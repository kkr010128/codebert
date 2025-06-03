import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N = int(readline())
S,T = readline().decode().rstrip().split()
ans = ''
for i in range(N):
    ans += S[i] + T[i]
print(ans)