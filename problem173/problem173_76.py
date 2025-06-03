n = int(input())
l = list(range(0,n+1))
print(sum([i for i in l if i % 3 != 0 and i % 5 != 0]))