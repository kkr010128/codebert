n=input()
c=[]
A=[]
for i in ['S ','H ','C ','D ']:
    for j in map(str,range(1,14)):
        A.append(i+j)   
for i in range(n):
    A.remove(raw_input())
for i in range(len(A)):
    print A[i]