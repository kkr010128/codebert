
s = input()
n = int(input())

hanten=0
s1=""
s2=""
for i in range(n):
    Q = input()
    if int(Q[0])==1:
        hanten+=1 
    elif int(Q[0])==2 :
        if hanten%2 == int(Q[2])-1 :
            s1= s1+Q[4]
        else:
            s2= s2+Q[4]

s1 = s1[::-1]
s = s1+s+s2

if hanten%2 :
    s = s[::-1]
print(s)        



