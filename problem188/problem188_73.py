x,y,a,b,c=map(int,input().split())

a_list=list(map(int,input().split()))
a_list=sorted(a_list)
b_list=list(map(int,input().split()))
b_list=sorted(b_list)
a_list=a_list[-x:]
b_list=b_list[-y:]
c_list=list(map(int,input().split()))
for i in range(c):
    c_list[i]=-c_list[i]
import heapq
heapq.heapify(a_list)
heapq.heapify(b_list)
heapq.heapify(c_list)

flag=True
while flag and c_list:
    x=heapq.heappop(c_list)
    x=x*(-1)
    #ｃ_listの中でのもっとも大きい値
    min_a=heapq.heappop(a_list)
    min_b=heapq.heappop(b_list)
    if min(min_a,min_b)>=x:
        flag=False
        heapq.heappush(a_list,min_a)
        heapq.heappush(b_list,min_b)
    else:
        if min_a>=min_b:
            heapq.heappush(a_list,min_a)
            heapq.heappush(b_list,x)
         
        elif min_a<min_b:
            heapq.heappush(b_list,min_b)
            heapq.heappush(a_list,x)

sum_a=sum(list(a_list))
sum_b=sum(list(b_list))

print(sum_a+sum_b)
            

    


