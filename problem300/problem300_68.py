a, b = map(int, input().split())
roota = int(a ** 0.5)

def pcheck(n):
    rootn = int(n ** 0.5)
    for i in range(2, rootn + 2):
        if n % i == 0:
            return False
    return True

pa = []
for i in range(2, roota + 2):
    if a % i == 0:
        pa.append(i)
        while a % i == 0:
            a //= i
if (pcheck(a) == True) & (a != 1):
    pa.append(a)
cd = []
for i in range(len(pa)):
    if b % pa[i] == 0:
        cd.append(pa[i])
print(len(cd) + 1)