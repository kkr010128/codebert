from numba import jit

@jit
def solve():
    n, k = map(int,input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    max_score = -10**10

    for i in range(n):
        count = 1
        val = c[i]

        next_i = p[i] -1
        while next_i != i:
            count += 1
            val += c[next_i]
            next_i = p[next_i] - 1
        
        if val > 0:
            loop_num = (k//count -1)
            tmp_score = loop_num * val
            max_score = max(tmp_score, max_score)
            num = k%count+count

        else:
            tmp_score = 0
            num = min(k, count)

        next_i = i
        for _ in range(num):
            next_i = p[next_i] - 1
            tmp_score += c[next_i]
            max_score = max(tmp_score, max_score)
    
    print(max_score)

solve()