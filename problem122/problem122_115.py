n = int(input())
array = list(map(int,input().split()))
q = int(input())
sums = sum(array)
cnt = [0]*(10**5+1)
for i in array:
    cnt[i] += 1
for j in range(q):
    b,c = map(int,input().split())
    sums += cnt[b]*(c-b)
    cnt[c] += cnt[b]
    cnt[b] = 0
    print(sums)