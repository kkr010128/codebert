n=int(input())
a=[i for i in input().split(" ")]
b=a.copy()
flg=1

while flg:
    flg=0
    for j in range(n-1,0,-1):
        if a[j][1] < a[j-1][1]:
           a[j-1],a[j]=a[j],a[j-1]
           flg=1  

for i in range(n):
    mi=i
    for j in range(i,n):
        if b[j][1] < b[mi][1]:
            mi = j
    if i != mi:
        b[i],b[mi]=b[mi],b[i]

print(" ".join([str(i) for i in a]))
print("Stable")
print(" ".join([str(i) for i in b]))
if a==b:
    print("Stable")
else:
    print("Not stable")