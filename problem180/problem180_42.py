l=input("").split(" ")
n=int(l[0])
k=int(l[1])
s=n%k
ss=k-s
if(s<ss):
    print(s)
else:
    print(ss)