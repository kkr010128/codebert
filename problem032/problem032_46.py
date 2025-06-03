n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

for p in range(1, 3 + 1):
    s = sum([(pow(abs(x[i] - y[i]), p)) for i in range(n)])
    print('{0:.6f}'.format(pow(s, 1 / p)))

print('{0:.6f}'.format(max([abs(x[i] - y[i]) for i in range(n)])))