import sys
input=sys.stdin.readline
count=0
res=""
str=input()
list=[]
for i in range(len(str)):
  list.append(str[i])
for i in range(len(str)):
  if str[i]=="?":
    if i==0:
      if list[1]=="D":
        list[0]="P"
      else:
        list[0]="D"
    elif i+1==len(str):
      list[i]="D"
    else:
      if list[i-1]=="P":
        list[i]="D"
      else:
        if list[i+1]=="D" or list[i+1]=="?":
          list[i]="P"
        else:
          list[i]="D"
for i in range(len(str)):
  res+=list[i]
print(res)
