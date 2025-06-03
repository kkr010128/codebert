nxt = input().split()
#print(nxt)
N = int(nxt[0]) 
X = int(nxt[1])
T = int(nxt[2])
#print(N,X,T)
tmp = N/X - int(N/X)
if tmp == 0:
    counter = int(N/X)
else:
    counter = int(N/X) + 1
#print(counter)
print(counter * T)