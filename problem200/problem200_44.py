A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = []
for i in range(M):
    x, y, c = map(int, input().split())
    answer.append(a[x-1]+b[y-1]-c)

print(min(min(answer), min(a)+min(b)))