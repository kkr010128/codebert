N = int(input())
S,T = input().split()
ans = ["a"]*(N*2)
for i in range(N) : 
    ans[2*i] = S[i]
    ans[2*i+1] = T[i]
print(''.join(ans))