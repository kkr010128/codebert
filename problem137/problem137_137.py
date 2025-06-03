n = int(input())

al = []
bl = []
for i in range(n):
    a,b = [int(i) for i in input().split()]
    al.append(a)
    bl.append(b)
    
al = sorted(al)
bl = sorted(bl)

median_a = al[n//2]if n % 2 else (al[n // 2] + al[n//2 - 1]) / 2 
median_b = bl[n//2]if n % 2 else (bl[n // 2] + bl[n//2 - 1]) / 2 

if n % 2:
    print(int((median_b - median_a + 1)))
else:
    print(int((median_b - median_a) * 2 + 1))