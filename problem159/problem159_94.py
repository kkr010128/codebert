n=int(input())
m=100
y=0

while m < n:
    m += m//100
    y += 1
print(y)