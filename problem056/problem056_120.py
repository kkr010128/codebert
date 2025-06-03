vec1 = []
vec2 = []

n, m = map(int, input().split())
for x in range(1, n+1):
    vec1.append(list(map(int, input().split())))

for y in range(m):
    vec2.append(int(input()))

for j in vec1:
    result = 0
    for w, z in zip(j, vec2):
        result += w * z
    print(result)

