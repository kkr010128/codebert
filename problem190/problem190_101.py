s = input()

def kaibun(s):
    if s == s[::-1]:
        return 1
    else:
        return 0
        
q = len(s)
d = int((q-1)/2)
ket = s[0:d]
mat = s[int((q+1)/2):q]

if (kaibun(s) + kaibun(ket) + kaibun(mat)) == 3:
    print('Yes')
else:
    print('No')
