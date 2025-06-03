# A Odds of Oddness
n = int(input())
c = []
for i in range(1,n+1):
    if i % 2:
        c.append(i)
x = len(c)/n
print(x)
