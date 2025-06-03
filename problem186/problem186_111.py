K, N = map(int, input().split())

A_list = list(map(int, input().split()))
A_gap_max = 0
ans = 0

for i in range(N-1):
    A_gap_temp = A_list[i+1] - A_list[i]
    if A_gap_temp > A_gap_max:
        A_gap_max = A_gap_temp
    ans += A_gap_temp 
A_gap_temp = A_list[0] + K - A_list[N-1]
if A_gap_temp > A_gap_max:
    A_gap_max = A_gap_temp
ans += A_gap_temp 
    
ans -= A_gap_max
print(ans)
