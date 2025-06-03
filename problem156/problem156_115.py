x=int(input())
A=[i**5 for i in range(-2000,2000)]
for i in range(4000):
    for j in range(i):
        if A[i]-A[j]==x:
            print(*[i-2000,j-2000]);exit()
