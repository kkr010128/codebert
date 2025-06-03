N, M = map(int, input().split()) 
ans = []
if M % 2 != 0:
    for i in range((M + 1)//2):
        ans.append((1 + i, M + 1 - i))
        
    for j in range((M - 1)//2):
        ans.append((M + 2 + j, 2*M + 1 - j))
else:
    for i in range(M//2):
        ans.append((1 + i, M + 1 - i))
        ans.append((M + 2 + i, 2*M + 1 - i))
              
for i in range(M):
    print(*ans[i])