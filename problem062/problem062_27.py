N=[]
while True:
    n=raw_input()
    if n=='0':
        break
    N.append(n)
for i in range(len(N)):
    print('%d'%sum(map(int,N[i])))