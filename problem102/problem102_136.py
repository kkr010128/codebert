n,k=map(int,input().split())
lst_1=list(map(int,input().split()))
# print(lst_1)
lst_2=[]
for i in range(n-k):
    temp=1
    temp=lst_1[i+k]/lst_1[i]
    lst_2.append(temp)
for i in lst_2:
    if i>1:
        print("Yes")
    else:print("No")
