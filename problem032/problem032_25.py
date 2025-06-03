dim = int(input())
a, b = list(map(int, input().split())), list(map(int, input().split()))
dif = [ abs(x-y) for x, y in zip(a, b)]
print("%lf\n%lf\n%lf\n%lf" % (sum(dif), 
                                sum([i ** 2 for i in dif]) ** (1 / 2),
                                sum([i ** 3 for i in dif]) ** (1 / 3),
                                max(dif)
                                ))
