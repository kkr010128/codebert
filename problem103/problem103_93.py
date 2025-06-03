n = int(input())
a = list(map(int, input().split()))
money = 1000
kabu = 0
for i in range(n-1):
    if a[i] < a[i+1]:
        kabu = money//a[i] * a[i+1] #持ち株数×時価
        money = (money % a[i]) + kabu
print(money)
        
   



