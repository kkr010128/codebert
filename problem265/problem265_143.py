#4
import sys
N = int(input())
x,y,k = 0,0,0

if N == 1:
    print(1)
    sys.exit()
elif N <= 12:
    print(N)
    sys.exit()
x = int(0.8*N)

for i in range(x,N):
    k = str(i*108)
    if int(k[0:-2]) == N:
        print(i)
        y +=1
        break

if y !=1:
    print(":(")
