money=100000
n=int(input())
for day in range(n):
    money+=money*0.05
    money=-(-money//1000)*1000
print(int(money))
