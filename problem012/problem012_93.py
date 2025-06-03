import math
def prime(num):
    judge = True
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            judge = False
    return judge
    
n = int(input())
cnt = 0
ns=[]
for i in range(n):
    num = int(input())
    if prime(num):
        cnt += 1
print(cnt)
