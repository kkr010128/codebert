N,K = map(int,input().split())
i = N%K
j = -i+K
print(min(i,j))