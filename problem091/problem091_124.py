n = int(input())
l = [int(li) for li in input().split(' ')]

def is_unique(a, b, c):
    return (a != b) and (a != c) and (b != c)

def is_triangle(a, b, c):
    return (a + b > c) and (b + c > a) and (c + a > b)

cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            a, b, c = l[i], l[j], l[k]
            if is_unique(a, b, c) and is_triangle(a, b, c):
                cnt += 1
print(cnt)
