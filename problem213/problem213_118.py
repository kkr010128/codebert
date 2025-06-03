N = int(input())
a = list(map(int,input().split()))
loc = round(sum(a) / N)
print(sum(map(lambda x: (x - loc) ** 2,a)))