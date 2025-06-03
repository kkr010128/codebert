number = int(input())
list1,list2 = input().split(" ")
str=""
for i in range(number):
  str=str+list1[i]+list2[i]
print(str)