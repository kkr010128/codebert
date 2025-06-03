n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

for p in range(1,4):
    print("{0:.6f}".format(pow(sum([pow(abs(x[i] - y[i]), p) for i in range(n)]) ,1/p)))
print("{0:.6f}".format(pow(pow(max([abs(x[i] - y[i]) for i in range(n)]),n),1/n)))