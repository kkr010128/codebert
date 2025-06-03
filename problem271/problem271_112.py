import string

n = int(input())
s = input()

alpha = [chr(i) for i in range(65, 65+26)]
res = ""

for c in s:
    po = alpha.index(c)
    po = po + n
    if po > 25:
        po = po - 26
    res = res + alpha[po]
    
print(res)