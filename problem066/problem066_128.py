a=[]

while True:
    tmp99=[]
    tmp0=input()
    if tmp0=="-":
        break
    tmp99.append(list(tmp0))
    tmp1=int(input())
    tmp99.append(tmp1)
    for i in range(tmp1):
        tmp99.append(int(input()))
    a.append(tmp99)
for i in a:
    for j in i[2:]:
        i[0]=i[0][j:]+i[0][:j]
for i in a:
    print("".join(i[0]))
