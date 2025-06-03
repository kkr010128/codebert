import math

while True:
    n = int(input());
    if n == 0:
        break;
        
    A = list(map(int, input().split()));


    h = sum(A) / len(A);
    k = 0;
    for j in range(0,n):
        k += (A[j] - h)**2;
    print(math.sqrt(k/n));


