S = input().rstrip() + "#"
s0 = S[0]
A, cnt = [], 1
for s in S[1:]:
    if s==s0: cnt+=1
    else: A.append(cnt); cnt=1
    s0 = s
res, st = 0, 0
if S[0]==">":
    res += A[0]*(A[0]+1)//2
    st=1
for i in range(st,len(A),2):
    if i+1==len(A): res += A[i]*(A[i]+1)//2; break
    p, q = A[i], A[i+1]
    if p < q:
        res += q*(q+1)//2 + p*(p-1)//2
    else:
        res += q*(q-1)//2 + p*(p+1)//2
print(res)

