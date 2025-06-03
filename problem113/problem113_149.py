import time
import  random
def main():
    start = time.time()
    for d in range(D):
        res[d] = d%26
    ma = check(res)
    
    while 1:
        idx1 = random.randint(0,D-1)
        idx2 = random.randint(0,D-1)
        if idx1==idx2:
            continue
        taihi = res[idx1]
        res[idx1] = res[idx2]
        res[idx2] = taihi
        tmp = check(res)
        if tmp > ma:
            ma = tmp
        else:
            res[idx2] = res[idx1]
            res[idx1] = taihi
        if time.time() - start > 1.75:
            break
    return res

def check(res):
    last = [0] * 26
    score = 0
    for d in range(D):
        sd = s[d]
        score += sd[res[d]]
        last[res[d]] = d+1
        for i in range(26):
            score -= c[i]*(d+1-last[i])
    return score

if __name__ == '__main__':
    D = int(input())
    c = list(map(int, input().split()))
    s = [list(map(int, input().split())) for _ in range(D)]
    res = [0] * D
    ans = main()
    for val in ans:
        print(val+1)