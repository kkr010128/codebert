n = int(input())
x = list(map(int, input().split()))
print(sum((xi - round(sum(x)/n))**2 for xi in x))