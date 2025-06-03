#a問題(できなかった)
s = input()
p=s[0]=='R'
q=s[1]=='R'
r=s[2]=='R'

if p and q and r==True:
    print(3)
elif (p and q)or(q and r)==True:
    print(2)
elif p or q or r ==True:
    print(1)
else:
    print(0)


