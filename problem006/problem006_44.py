n = int(input())
x = 100000
for i in range(n):
    x = x * 1.05
    if x % 1000 != 0:
        x=x+1000-(x%1000)
print(int(x))

