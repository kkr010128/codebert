n = int(input())
a = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

value = []
for i in range(2 ** n):
    ans = 0
    for j in range(n):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            ans += a[j]
    value.append(ans)  

for mm in range(len(m)):          
    if m[mm] in value:
        print("yes")
    else:
        print("no")
