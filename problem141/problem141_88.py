n = int(input())
ai = [int(i) for i in input().split()]

tmp = 0
ans = 0
old = 0

a_mnmx = [[0 for i in range(2)] for j in range(n+1)]
#print(a_max)
old = ai[n]

a_mnmx[n][0] = old
a_mnmx[n][1] = old

for i in range(n):
    a_mnmx[n-i-1][0] = (a_mnmx[n-i][0]+1)//2 + ai[n-i-1]
    a_mnmx[n-i-1][1] = a_mnmx[n-i][1] + ai[n-i-1]
    
#print(a_mnmx)

if a_mnmx[0][1] < 1 or a_mnmx[0][0] > 1:
    print(-1)
    exit()

old = 1
ans = 1

for i in range(n):
    old = min(a_mnmx[i+1][1],old*2)
    ans += old
    old -= ai[i+1]
    #print(old)
    
print(ans)