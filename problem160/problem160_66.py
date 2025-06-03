number=list(map(int,input().split()))
n,m,q=number[0],number[1],number[2]
nums=[]
for i in range(q):
    tmp=list(map(int,input().split()))
    nums.append(tmp)
answer=0
mid=0
List1=[]
for i in range(m):
  List1.append(i)
import itertools
for i in list(itertools.combinations_with_replacement(List1,n)):
    mid=0
    for j in range(q):
        if i[nums[j][1]-1]-i[nums[j][0]-1]==nums[j][2]:
            mid+=nums[j][3]
    answer=max(mid,answer)
    
print(answer)
