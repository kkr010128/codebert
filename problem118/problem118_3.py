n = int(input())

answer = 0
for i in range(1, n+1):
    md = n // i

    answer += i * (md *(md+1) // 2)

print(answer)