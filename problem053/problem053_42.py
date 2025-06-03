N = int(input())
n = input().split()
line = '{0}'.format(n[-1])
for i in range(1,N):
    line += ' {0}'.format(n[N-i-1])
print(line)