N = int(input())

h = [2,4,5,7,9]
p = [0,1,6,8]
b = [3]

if h.count(N%10)==1:
    print('hon')
if p.count(N%10)==1:
    print('pon')
if b.count(N%10)==1:
    print('bon')