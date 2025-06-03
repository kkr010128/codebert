N = int(input())
sqrt_N = int(N ** 0.5)

dividers_for_N = set()
ans_set = set()

for i in range(1, sqrt_N + 1):
    if (N - 1) % i == 0:
        ans_set.add(i)
        ans_set.add((N - 1) // i)

    if N % i == 0:
        dividers_for_N.add(i)
        dividers_for_N.add(N // i)

dividers_for_N -= {1}
ans_set -= {1}

for i in dividers_for_N:
    num = N
    while num % i == 0:
        num //= i
    if num % i == 1:
        ans_set.add(i)

ans = len(ans_set)

print(ans)