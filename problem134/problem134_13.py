N=int(input())
ans =1
A = list(map(int,input().split()))
for i in A:
        if i == 0:

               print(0)
               exit()
for i in A:
      
       ans *=i
       if ans >10**18:
               print(-1)
               exit()
print(ans)
