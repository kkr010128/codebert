N = int(input())
A = list(map(int,input().split()))
B = [[A[i],i+1]for i in range(N)]
B.sort()
ans = [B[i][1]for i in range(N)]
print(" ".join(map(str,ans)))