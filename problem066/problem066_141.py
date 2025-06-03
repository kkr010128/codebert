Str=[]
H=[]
h=[]
while True:
    x=input()
    if x=='-':
        break
    Str.append(x)
    m=int(input())
    for i in range(m):
        x=int(input())
        h.append(x)
    H.append(h)
    h=[]
for i in range(len(Str)):
    a=Str[i]
    for j in range(len(H[i])):
        a=''.join([a[H[i][j]:],a[:H[i][j]]])
    Str[i]=a
for str in Str:
    print(str)