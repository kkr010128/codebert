n = int(input())
aas = list(map(int, input().split()))
cnts = [0]*(n+1)
for i in range(n):
    cnts[aas[i]] += 1
t = 0
for i in range(1,n+1):
    tmp = cnts[i]
    t += tmp*(tmp-1)//2
for i in range(n):
    tmp = cnts[aas[i]]
    print(int(t-tmp*(tmp-1)/2*(1-1/tmp*(tmp-2))))