n, k = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(min(50, k)):
    l = [0]*(n+1)
    for i in range(n):
        l[max(i-a[i], 0)] += 1 #光の届く距離（後ろ）
        l[min(i+a[i]+1, n)] -= 1 #光が届かなくなる距離(前)
    add = 0
    for i in range(n):
        add += l[i] #光の届いている電球の数を累積
        a[i] = add
print(*a)
