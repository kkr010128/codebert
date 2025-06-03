a,b,c = [int(i) for i in input().split()]
d = []
for i in range(1,int(c**0.5)+1):
    if i **2 == c:
        d.append(i)
        continue
    if c%i == 0:
        d.extend([i,c//i])
d.sort()
e = [i for i in d if a<=i<=b]
print(len(e))

