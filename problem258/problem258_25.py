import sys
#input = sys.stdin.buffer.readline
N = int(input())
temp = 5
ans = 0
if N%2:
    print(0)
    quit()
else:
    N = N//2
    while temp <= N:
        ans += N//temp
        temp *= 5
print(ans)