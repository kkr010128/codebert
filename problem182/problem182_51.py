nkc=input().split()
K=int(nkc[1])
C=int(nkc[2])
s=input()
workday_list=[]
for i,youso in enumerate(s) :
  if youso=='o' :
    workday_list.append(i+1)
    

s=1

current_num=0
current_num1=1
list1=[]
list1.append(workday_list[0])
while(s<K) :
  
  if current_num1>=len(workday_list):
    break
  elif workday_list[current_num1]-workday_list[current_num]>C :
    current_num=current_num1
    list1.append(workday_list[current_num1])
    s+=1
  else :
    current_num1=current_num1+1
m=1  

current_num2=len(workday_list)-1
current_num3=len(workday_list)-2
list2=[]
list2.append(workday_list[-1])
while(m<K) :
  
  if current_num3<0:
    break
  elif workday_list[current_num2]-workday_list[current_num3]>C :
    current_num2=current_num3
    list2.append(workday_list[current_num3])
    m+=1
  else :
    current_num3=current_num3-1

list2.reverse()

flag=True
for i in range(len(list1)) :
  if list1[i]==list2[i] :
    flag=False
    print(list1[i])
if flag :
  print()
