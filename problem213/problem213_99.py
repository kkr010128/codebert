N = int(input())
X = list(map(int, input().split()))
a = int(sum(X) / N)
b = a + 1
A, B = 0, 0
for x in X:
    A += (x - a) ** 2
    B += (x - b) ** 2
ans = min(A, B)
print(ans)