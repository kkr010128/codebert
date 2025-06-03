s1 = input()
n1 = len(s1)
s2 = s1[:(n1-1)//2]
n2 = len(s2)
s3 = s1[-(n1-1)//2:]
n3 = len(s3)
f1, f2, f3 = True, True, True
for i in range((n1-1)//2):
    if s1[i] != s1[-i-1]:
        f1 = False
        break
for i in range(n2//2):
    if s2[i] != s2[-i-1]:
        f2 = False
        break
for i in range(n3//2):
    if s3[i] != s3[-i-1]:
        f3 = False
        break
if f1 and f2 and f3:
    print('Yes')
else:
    print('No')