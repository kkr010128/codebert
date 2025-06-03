N = int(input())
A = map(int, input().split())

result = [0] * N
for i, v in enumerate(A):
    result[v-1] = str(i + 1)

print(' '.join(result))
