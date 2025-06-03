a,b,m=map(int,input().split())
a_list=list(map(int,input().split()))
b_list=list(map(int,input().split()))

min_num=min(a_list)+min(b_list)
for i in range(m):
  x,y,c=map(int,input().split())
  num = a_list[x-1] + b_list[y-1] -c
  min_num=min(min_num,num)
  
print(min_num)