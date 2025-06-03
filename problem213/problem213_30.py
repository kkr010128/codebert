n = int(input())
(*x,) = map(int, input().split())
a = round(sum(x) / n)
print(sum(((i - a) ** 2) for i in x))