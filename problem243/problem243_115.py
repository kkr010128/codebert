#template
def inputlist(): return [int(j) for j in input().split()]
#template
N = int(input())
lis = ['0']*N
time = [0]*N
for i in range(N):
    lis[i],time[i] = input().split()
sing = input()
index = -1
for i in range(N):
    if lis[i] == sing:
        index = i
        break
ans = 0
for i in range(index+1,N):
    ans += int(time[i])
print(ans)