n = int(input())
a = input().split()
a = [int(i) for i in a]
a.sort()
flg = "YES"
for i in range(n-1):
    if (a[i] == a[i+1]):
        flg = 'NO'
        break
print(flg)