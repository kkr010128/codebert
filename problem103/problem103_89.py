n = int(input())
a = list(map(int, input().split()))

money = 1000
kabu = 0
for i in range(n-1):
    if a[i] < a[i+1]:
        kabu += money//a[i]
        money %= a[i]
    else:
        money += kabu * a[i]
        kabu = 0

if kabu > 0:
    money += kabu*a[n-1]
print(money)