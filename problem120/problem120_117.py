n,k = input().split()
k = int(k)-1
a = list()
a = input().split(" ")
b = list()
for i in a:
    b.append(int(i))
b.sort()
sum = 0
while k>=0:
    sum += b[k]
    k -= 1
print(sum)