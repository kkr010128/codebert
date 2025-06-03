N = int(input())
l = input().split()
l2 = l[:]
for j in range(N):
    for i in range(N-1):
        if l[i][1] > l[i+1][1]:
            l[i], l[i+1] = l[i+1], l[i]
for i in range(0,len(l)-1):
    print(l[i],end=' ')
print(l[N-1])
print("Stable")

for j in range(0,len(l2)-1):
    min = l2[j][1]
    a = j
    for i in range(j,len(l2)):
        if min > l2[i][1]:
            min = l2[i][1]
            a = i
    l2[j],l2[a] = l2[a],l2[j]
for i in range(0,len(l2)-1):
    print(l2[i],end=' ')
print(l2[N-1])
if l==l2:
    print("Stable")
else:
    print("Not stable")

