N = int(input())
num = []
for i in range(1, 9+1):
     for j in range(1, 9+1):
         num.append(i * j)

if N in num:
    print("Yes")
else:
    print("No")