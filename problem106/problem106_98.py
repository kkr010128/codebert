N = int(input())
Ans = [0] * (N + 1)


def calc(a, b, c):
    return a ** 2 + b ** 2 + c ** 2 + a * b + b * c + c * a


for i in range(1, N):
    for j in range(1, N):
        for k in range(1, N):
            x = calc(i, j, k)
            if x > N:
                break
            Ans[x] += 1

for a in Ans[1:]:
    print(a)