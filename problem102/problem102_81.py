# cook your dish here
n,k=input().split()
n=int(n)
k=int(k)
l=list(map(int,input().split()))
for j in range(n):
    if k+j==n:
        break
    if l[k+j]>l[j]:
        print("Yes")
    else:
        print("No")
    
      
   


    
