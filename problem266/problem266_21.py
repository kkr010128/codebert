x = int(input())
a,b = x//100, x%100
print(1 if a*5 >= b else 0)