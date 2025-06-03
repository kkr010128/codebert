from collections import Counter

#input
N,K = list(map(int,input().split()))
R,S,P = list(map(int,input().split()))

T = list(input())
T_ =T.copy()

# N=2*10**5
# T=[random.choice(['s', 'r', 'p']) for _ in range(N)]

check=set(['s', 'r', 'p'])

#得点
point={'r':P,'s':R,'p':S}
point

T_point = [0]*N
for n in range(N):
    T_point[n]=point[T[n]]
    
for k in range(K,N):
    check_out = set()
    if T[k] == T[k-K]: # K回前の手と同じ場合
        check_out.add(T[k])
        if k+K < N:
            check_out.add(T[k+K])
            
        check_out=check-check_out
        
        T[k]=list(check_out)[0]
         
ans=0

for t in range(len(T)):
    if T[t] == T_[t]:
        ans += point[T[t]]
print(ans)
