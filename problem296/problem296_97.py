import math
S=input()
K=int(input())

ss=S*2

ss=[a for a in ss]
answer=0
N=len(ss)
for n in range(N-1):
    if ss[n]==ss[n+1]:
        answer+=1
        ss[n+1]=0

sss=S*3

sss=[a for a in sss]
suuji=0
N=len(sss)
for n in range(N-1):
    if sss[n]==sss[n+1]:
        suuji+=1
        sss[n+1]=0

number=0
s=[a for a in S]
N=len(s)
for n in range(N-1):
    if s[n]==s[n+1]:
        number+=1
        s[n+1]=0
if K==1:
    print(number)
else:
    if answer - number == suuji - answer:
        print(number + (answer - number) * (K - 1))
    else:
        if K % 2 == 0:
            print(number + (answer - number) * (K//2)+(suuji-answer)*(K//2-1))
        else:
            print(number + (answer - number) * (K//2)+(suuji-answer)*(K//2))

