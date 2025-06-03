import sys

x=sys.stdin.readline()

arr=x.split()

arrInt=list()
#print(arr, type(arr))
for i in arr:
   # print(i)
    arrInt.append(int(i))

#print(arrInt,type(arrInt))
    arrInt.sort()
print(' '.join(map(str,arrInt)))



