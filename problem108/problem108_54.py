N=input()
n=int(N)
k=int(n%1000)
if k==0:
    print(0)
else:
    print(1000-k)