def one_int():
    return int(input())

N=one_int()
num=int(N/100) 
amari = N % 100
if num*5 < amari:
    print(0)
else:
    print(1)