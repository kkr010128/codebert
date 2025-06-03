NK = input()
num = NK.split()
N = num[0]
K = num[1]

P = input()
Pn = P.split()
#print(Pn)

Pn_a = [int(i) for i in Pn]
Pn_b = sorted(Pn_a)

price = 0

for i in range(int(K)):
    price += int(Pn_b[i])
    
print(price)
