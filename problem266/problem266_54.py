x = int(input())
a = x//100
b = x%100
if b <= 5*a:
    print(1)
    exit()
print(0)