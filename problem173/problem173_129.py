N = int(input())
N=N+1

a_ =sum(list(range(1,N,1)))
a_3=sum(list(range(3,N,3)))
a_5=sum(list(range(5,N,5)))
a_15=sum(list(range(15,N,15)))
ans=a_ + a_15 -(a_3+a_5)
print(ans)