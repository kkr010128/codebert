N = int(input())
towns = [tuple(map(int, input().split())) for _ in range(N)]

total_distance = 0
count = 0
for start in range(N-1):
    for end in range(start+1, N):
        start_x, start_y = towns[start]
        end_x, end_y = towns[end]

        total_distance += ((end_x - start_x)**2 + (end_y - start_y)**2)**0.5
        count += 1

answer = total_distance * ((N - 1) / count)
print(answer)