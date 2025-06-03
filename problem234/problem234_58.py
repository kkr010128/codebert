n = input()

if int(n)<10:
    print(n)
    exit()

matubi=int(n[-1])
sentou=int(n[0])
keta=len(n)

if n[1:keta-1]=="":
    aida=0
else:
    aida=int(n[1:keta-1])

n=int(n)
def cnt(saisyo,saigo):
    kotae=(10**(keta-2)-1)/9
    if saisyo<sentou:
        kotae+=10**(keta-2)
    elif saisyo==sentou:
        tmp=saisyo*10**(keta-1)+saigo
        while True:
            if str(tmp)[0]==str(saisyo) and tmp<=n:
                kotae+=1
            else:
                break
            tmp+=10
    if saisyo==saigo:
        kotae+=1
    return kotae

ans=0

import itertools
for seq in itertools.product(range(1,10),range(1,10)):
    ans+=cnt(seq[0],seq[1])*cnt(seq[1],seq[0])

print(int(ans))