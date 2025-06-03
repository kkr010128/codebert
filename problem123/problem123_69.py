N=int(input())
a = list(map(int,input().split()))
s = a[0]
for i in range(1,len(a)):
    s ^= a[i]
    #print(a[i])
#print(s)
for i in range(len(a)):
    #print(s,a[i])
    ans = s^a[i]
    print(ans,end=" ")
