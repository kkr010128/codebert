n = int(input())
a = []
for _ in range(n):
    a.append([list(map(int,input().split())) for __ in range(int(input()))])
l = []
for i in range(2**n):
    flag2 = 0
    for j in range(n):
        if i >> j & 1 == 1:
            flag1 = 0
            for k in a[j]:
                if i >> (k[0]-1) & 1 != k[1]:
                    flag1 = 1
                    flag2 += 1
                    break
            if flag1 : break
        
    if flag2 == 0 :l.append(list(bin(i)).count('1'))
print(max(l))