a, b = map(int, input().split())
mat = [map(int, input().split()) for i in range(a)]
vec = [int(input()) for i in range(b)]
for row in mat:
    print(sum([x*y for x, y in zip(row, vec)]))
