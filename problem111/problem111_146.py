n = int(input())
la = list(map(int, input().split()))
la.sort(reverse=True)

answer = la[0]
for i in range(n - 2):
    answer += la[1 + i // 2]

print(answer)


