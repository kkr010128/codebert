#coding:utf-8

nyu =""
moji =[]
s1 =[]
s2 =[]
n= 0
a= 0
while nyu != "-":
    nyu = input().rstrip()
    if nyu =="-":
#        print("".join(moji))
        break

    n = int(input().rstrip())
    moji = list(nyu)

    for i in range(n):
        a = input().rstrip()
        s1 =moji[:int(a)]
        s2 =moji[int(a):]
        moji= list("".join(s2) + "".join(s1))
#        print(moji)

    print("".join(moji))