n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
for p in range(3):
    print(sum(abs(x[i] - y[i]) ** (p+1) for i in range(n)) ** (1/(p+1)))
print(max(abs(x[i] - y[i]) for i in range(n)))
