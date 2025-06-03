lst=[]
while True:
    lst.append(input())
    if "0" in lst:
        break
lst=lst[:-1]
for i in lst:
    sum=0
    for j in range(len(i)):
        sum+=int(i[j])
    print(sum)
