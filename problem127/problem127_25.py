a,b = map(int,input().split())
c="入力が間違っています。"
d="鶴が"
e="匹で、亀が"
f="匹です。"
 
k=b//2-a
t=2*a-b//2
if k<0 or t<0 or b%2!=0:
    print('No')
else:
    print('Yes')