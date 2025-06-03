N,A,B=list(map(int, input().split()))
ct=N//(A+B)
res=N%(A+B)
print(A*ct + min(A,res))