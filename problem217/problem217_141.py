n = int(input())
a = list(input().split())
tmp = []
flag = 0
for i in range(n):
    if int(a[i]) % 2 == 0:
        tmp.append(a[i])
for j in range(len(tmp)):
    if int(tmp[j]) % 3 == 0 or int(tmp[j]) % 5 == 0:
        continue
    else:
        flag = 1
if flag == 1 : print("DENIED")  
else : print("APPROVED")