import math
def div(x, y): #x>y
    A = 1
    for i in range(1, int(math.sqrt(x))+1):
        if x % i == 0 and y % i == 0:
            A = max(A, i)
        j = int(x/i)
        if x % j == 0 and y % j == 0:
            A = max(A, j)
    return A
x, y = map(int, input().split(" "))
print(div(x,y))



