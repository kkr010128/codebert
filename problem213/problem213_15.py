a = int(input())
n = list(map(int, input().split()))
m = round(sum(n) / len(n))
print(sum((i-m) ** 2 for i in n))
