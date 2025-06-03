N,R=input().split()
n,r=int(N),int(R)

if n>=10:
    print(r)
else:
    print(r+100*(10-n))