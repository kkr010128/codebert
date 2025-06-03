import math
i = 0
k = 0
q = 0
while k == 0 :
    N = int(input())
    if N == 0 :
        k = k + 1
    else :
        S = list(map(float, input().split()))        
        while k ==0 and i < N :
            m = sum(S) / N
            q = q + ((S[i] - m)**2)
            i = i + 1
        print(math.sqrt(q / N))
        q = 0
        i = 0

