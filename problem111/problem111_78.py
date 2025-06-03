N = int(input())
a = list(map(int, input().split()))

a.sort(reverse = True)
p = a[0]
for i in range(N-2): #-1は上記a[0]分、もう-1は最初の要素挿入は加点されないため。
    p += a[(i//2)+1]

print(p)