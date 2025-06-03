N = int(input())
sqrt_N = int(N ** 0.5)

dividers_for_N = []
ans_list = []

for i in range(1, sqrt_N + 1):
    if (N - 1) % i == 0:
        ans_list.append(i)
        if i != (N - 1) // i:
            ans_list.append((N - 1) // i)

    if N % i == 0:
        dividers_for_N.append(i)
        if i != N // i:
            dividers_for_N.append(N // i)

dividers_for_N.remove(1)
ans_list.remove(1)
        
for i in dividers_for_N:
    num = N
    while num % i == 0:
        num //= i
    if num % i == 1:
        ans_list.append(i)

ans = len(ans_list)

print(ans)