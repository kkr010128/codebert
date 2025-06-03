a,b,c=[int(x) for x in input().split(" ")]
k=int(input())
count=0
while b<=a:
    count+=1
    b*=2
while c<=b:
    count+=1
    c*=2
if count<=k:
    print("Yes")
else:
    print("No")

