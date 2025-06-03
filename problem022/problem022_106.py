N1=int(input())
array1=input().split()
N2=int(input())
array2=input().split()
c=0
for n2 in range(N2):
    if array2[n2] in array1:
        c+=1
print(c)
