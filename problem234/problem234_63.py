n = int(input())
start_end = [[0] * 10 for _ in range(10)]
for i in range(1,n+1):
    start = int(str(i)[0])
    end = int(str(i)[-1])
    start_end[start][end] += 1
ans = 0
for start in range(10):
    for end in range(start,10):
        if start == end:
            ans += start_end[start][end]**2
        else:
            ans += start_end[start][end] * start_end[end][start] * 2
print(ans)
