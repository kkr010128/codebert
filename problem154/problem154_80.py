n, k = map(int,input().split())
num = []
for i in range(k):
    j = int(input())
    list_1 = list(map(int,input().split()))
    for l in range(j):
        num.append(list_1[l])
        
ans = set(num)
print(n - len(ans))