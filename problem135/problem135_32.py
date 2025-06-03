from math import floor
A= input().split()
p = int(A[0])
q = round(float(A[1])*100)
t = p*q
t //= 100
print(t)