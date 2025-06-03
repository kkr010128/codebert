x = int(input())

a = x-x//100*100
print(1) if a//5 + (a%5!=0) <= x//100 else print(0)