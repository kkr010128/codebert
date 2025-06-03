X=int(input())
A=0
B=0
for i in range(-120,120):
    for k in range(-120,120):
        if i**5==X+k**5:
            A=i
            B=k
            break
print(A,B)