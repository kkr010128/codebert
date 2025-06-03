n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort(reverse=True)

#必要票数を求める
s = sum(a)
needed = s/4/m if s%(4*m) == 0 else s//(4*m)+1

for i in range(m):
    if a[i] < needed:
        print("No")
        break
else:
    print("Yes")
