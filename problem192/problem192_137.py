from collections import Counter

N=int(input())
list1=list(map(int,input().split()))

dic1=Counter(list1)

def choose2(n):
    return n*(n-1)/2

sum=0
for key in dic1:
    sum+=choose2(dic1[key])

for i in list1:
    print(int(sum-dic1[i]+1))