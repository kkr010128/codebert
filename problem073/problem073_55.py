n = int(input())
answer = 0
for idx1 in range(1, n+1):
    for idx2 in range(1, ((n+1) // idx1) + 1):
        c = n - (idx1 * idx2)
        if 1 <= c < n:
            answer += 1

print(answer)
