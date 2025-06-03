N,K,S=map(int,input().split())

if S==10**9:
  answer_list=[1]*N
else:
  answer_list=[S+1]*N
for i in range(K):
  answer_list[i]=S

print(*answer_list)