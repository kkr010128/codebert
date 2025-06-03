n = int(input())
a = list(map(int,input().split()))
ok = True
for i in range(n):
    if a[i] % 2 == 0 and a[i] % 3 != 0 and a[i] % 5 != 0:
        ok = False
if ok:
    print("APPROVED")
else:
    print("DENIED")