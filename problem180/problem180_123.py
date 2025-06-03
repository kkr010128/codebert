N, K = [int(a) for a in input().split()]

num_count = (N-N%K)//K
ans = min(abs(N - num_count*K), abs(N - (num_count+1)*K))
if num_count > 0:
    ans = min(abs(N - (num_count-1)*K), ans)
print(ans)