l = input().split(" ")
a = int(l[0])
b = int(l[1])
c = int(l[2])
k = int(input())
i = 0
while b <= a :
    b = b * 2
    i = i + 1
while c <= b :
    c = c * 2
    i = i + 1
if i <= k :
    print("Yes")
else:
    print("No")