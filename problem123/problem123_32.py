N = int(input())
alphas = list(map(int, input().split()))

all_xor = alphas[0] ^ alphas[1]
for i in range(2, N):
    all_xor = all_xor ^ alphas[i]
    
ans_list = []
for i in range(N):
    num_i = all_xor ^ alphas[i]
    ans_list.append(str(num_i))
    
ans = " ".join(ans_list)
print(ans)