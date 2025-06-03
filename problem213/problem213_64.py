#C-rally
N = int(input())
A = list(map(int, input().split()))
ans_min = 10**8
 
for i in range(min(A), max(A)+1):
    ans = 0
    for j in range(N):
        ans += (A[j] - i) ** 2
    
    if ans < ans_min:
        ans_min = ans
 
print(ans_min)
