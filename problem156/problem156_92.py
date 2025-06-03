def get(n):
    for i in range(-1000,1001):
        for j in range(-1000,1001):
            if(i**5-j**5==n):
                print(i,j)
                return
n=int(input())
get(n)