K=int(input())
ans = False
M,N = map(int,input().rstrip().split(" ")) 
#print(K,M,N)
for number in range(M,N+1):
    if number%K==0:
        ans = True
if ans:
    print("OK")
else:
    print("NG")