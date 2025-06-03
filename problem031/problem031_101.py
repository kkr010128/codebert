n = int(input())
while n:
    d  = [int(i) for i in input().split()]
    print((sum([(i - sum(d) / n)**2 for i in d]) / n)**0.5)
    n = int(input())
