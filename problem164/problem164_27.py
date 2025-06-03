A,B,C,D = list(map(int,input().split()))

Takahashi = C//B
if C%B != 0 :
    Takahashi += 1
    
Aoki = A//D
if A%D != 0 :
    Aoki += 1
    
# print(Takahashi,Aoki)

ans='No'
if Takahashi <= Aoki:
    ans = 'Yes'
    
print(ans)