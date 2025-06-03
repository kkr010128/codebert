count = {}
for i in range(int(input())):
    S = input()
    if S in count:
        count[S] += 1
    else:
        count[S] = 1
ans = max(count.values())
print(*sorted([A[0] for A in count.items() if A[1] == ans]))