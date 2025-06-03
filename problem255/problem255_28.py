n= int(input())
list=input()
strlist=list.split(' ')
output=''
for i in range(n):
    output=output+strlist[0][i]+strlist[1][i]


print(output)
