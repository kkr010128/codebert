a = input('')
N = []
num = 0
for i in a:
    N.append(i)
for j in range(0,len(N)):
    num += int(N[j])
if num%9 == 0:
    print('Yes')
else:
    print('No')