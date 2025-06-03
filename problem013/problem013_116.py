num=int(input())
r_1=int(input())
r_2=int(input())

max_profit=r_2-r_1
if r_1<r_2:
    min_value=r_1
else:
    min_value=r_2

for i in range(2,num):
    x=int(input())
    t=x-min_value
    if max_profit<t:
        max_profit=t
    if x<min_value:
        min_value=x
        
print(max_profit)