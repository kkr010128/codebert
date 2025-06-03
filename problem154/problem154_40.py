n, k = map(int, input().split())
count = [0] * n
for _ in range(k):
    kosu = int(input())
    pos = list(map(int, input().split()))
    for i in pos:
        count[i-1] +=1
ans = [True if i == 0 else False for i in count]
print(sum(ans))