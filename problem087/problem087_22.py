nstr=input()
keta=len(nstr)
wa=0
for i in range(keta):
    wa+=int(nstr[i])

ans="No"
if wa%9==0:
    ans="Yes"

print(ans)