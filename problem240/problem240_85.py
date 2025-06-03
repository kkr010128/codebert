N,M= map(int, input().split())
p = [0] * M
S = [0] * M
for i in range(M):
    p[i], S[i] = map(str, input().split())
    
AC_list=[0]*N
pena=[0]*N
for i in range(M):
    if S[i]=='AC':
        AC_list[int(p[i])-1]+=1
    else:
        if AC_list[int(p[i])-1]==0:
            pena[int(p[i])-1]+=1
num=0
num1=0
for i in range(N):
    if AC_list[i]!=0:
        num+=1
        num1+=pena[i]
print(num ,num1)