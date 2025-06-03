import math
A = []
N = int(input())
count = 0
for n in range(N):
    x = int(input())
    if x == 2:
        A.append(x)
        count += 1
    elif x % 2 == 0:
        pass
    elif x > 2:
        for i in range(3, int(math.sqrt(x))+2, 2):
            if x % i == 0:
                break
        else:
            count += 1
            A.append(x)
    
print(count)