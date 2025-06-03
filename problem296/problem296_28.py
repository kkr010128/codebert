S = input()
K = int(input())
now,cnt,num = S[0],1,0
for i in S[1:-1]:
    if i == now:
        cnt += 1
    else:
        num += cnt//2
        cnt = 1
        now = i
if S[-1] == now:
    num += (cnt+1)//2
else: num += cnt//2

S = S + S
now,cnt,num2 = S[0],1,0
for i in S[1:-1]:
    if i == now:
        cnt += 1
    else:
        num2 += cnt//2
        cnt = 1
        now = i
if S[-1] == now:
    num2 += (cnt+1)//2
else: num2 += cnt//2

length = len(S)//2
if len(set(S)) == 1 and length%2 == 1:
    print(length//2*K + K//2)
    exit()

if num2 - num*2 == 1:
    ans = K - 1 + num*K
else:
    ans = num*K
print(ans)