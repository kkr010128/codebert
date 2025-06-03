a_b_c=input().split()
a=int(a_b_c[0])
b=int(a_b_c[1])
c=int(a_b_c[2])
count=0
yakusuu_list=[]
for i in range(1,c+1):
    if c%i==0:
        yakusuu_list.append(i)
for i in yakusuu_list:
    if i in range(a,b+1):
        count+=1
print(count)
