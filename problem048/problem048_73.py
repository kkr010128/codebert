import sys
_ = sys.stdin.readline()
x=sys.stdin.readline()

arr=x.split()

arrInt=list()
#print(arr, type(arr))
for i in arr:
   # print(i)
    arrInt.append(int(i))

#print(arrInt,type(arrInt))
print(min(arrInt),max(arrInt),sum(arrInt))


