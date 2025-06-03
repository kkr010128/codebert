n,k=map(int,input().split())
lst_1=list(map(int,input().split()))
# print(lst_1)
for i in range(n-k):
    if(lst_1[i+k]>lst_1[i]):
        print("Yes")
    else:print("No")