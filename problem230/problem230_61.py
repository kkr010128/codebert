#silver fox
n,d,a=map(int,input().split())
from collections import deque
import math
data=[]
for i in range(n):
    x,h=map(int,input().split())
    data.append((x,h))
data=sorted(data,key=lambda x:x[0])
#data を位置の順番にソートしておく
add=0
damage_sum=0
damage_map=deque([])
for i in range(n):
    if damage_map:
        while damage_map and damage_map[0][0]<data[i][0]:
            k=damage_map.popleft()
            damage_sum-=k[1]
            
    if damage_sum<data[i][1]:
        p=math.ceil((data[i][1]-damage_sum)/a)
        damage_sum+=p*a
        add+=p
        #少なくともp回の攻撃を加えなくてはならない
        damage_map.append((data[i][0]+2*d,p*a))
        #data[i][0]+2*dのところまではp*aのダメージがプラスとして加算される
print(add)