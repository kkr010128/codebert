import math

n = int(input())

if int(math.ceil(n/1.08)*1.08) == n :
    print(math.ceil(n/1.08))
elif int(math.floor(n/1.08)*1.08) == n :
    print(math.floor(n/1.08))
else:
    print(":(")