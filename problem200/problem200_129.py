A, B, M = list(map(int, input().split()))
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

ans = min(a_list) + min(b_list)

for i in range(M):
    x, y, c = list(map(int, input().split()))
    cost = a_list[x - 1] + b_list[y - 1] - c
    if cost < ans:
        ans = cost
        
print(ans)