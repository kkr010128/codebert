n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
d = [abs(x[i] - y[i]) for i in range(n)]
for i in range(1,4):
    print('{0:f}'.format(sum(j ** i for j in d) ** (1 / i)))
print('{0:f}'.format(max(d)))