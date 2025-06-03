a,b = map(int,input().split())

astart, aend = int(a//0.08+1), int((a+1)//0.08) #[astart, aend)
bstart, bend = int(b//0.10+1), int((b+1)//0.10)

alst = set(range(astart,aend))
blst = set(range(bstart,bend))
share = alst & blst

if len(share) == 0:
    print(-1)
else:
    print(list(share)[0])