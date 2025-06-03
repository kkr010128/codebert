from collections import deque
k=int(input())
ans=deque([1,2,3,4,5,6,7,8,9])

for i in range(k):
    p=ans.popleft()
    if i==k-1:
        print(p)
    q=p%10
    if q==0:
        ans.append(10*p+0)
        ans.append(10*p+1)
    elif q==9:
        ans.append(10*p+8)
        ans.append(10*p+9)
    else:
        ans.append(10*p+q-1)
        ans.append(10*p+q)
        ans.append(10*p+q+1)

        


    



