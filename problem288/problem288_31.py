N = int(input())

for i in range(int(N**(1/2)),0,-1):
    if N%i == 0:
        break

print(i+N//i-2)
