n = int(input())

A = [0]*12000

for i in range(1,101):
    for j in range(1, 101):
        for k in range(1, 101):
            val = i**2 + j**2 + k**2 + i*j + i*k + j*k
            if val < 12000:
                A[i**2 + j**2 + k**2 + i*j + i*k + j*k] += 1

for i in A[1:n+1]:
    print(i)