
import random
import copy
import time
def evaluateSatisfaction(d, c, s, ans):
    score = 0
    last = [-1 for i in range(26)]
        
    for i in range(d):
        
        score += s[i][ans[i]]
        last[ans[i]] = i
        for j in range(26):
            if j != ans[i] or True:
                score -= c[j]*(i - last[j])
    return score
    
def valuationFunction(d,c,s,contestType,day,last):
    
    gain = s[day][contestType]
    #78 =  (1/2) * ((13*13) - 13)
    lost = c[contestType] * (78)
    return gain - lost

def Input():
    d = int(input())
    c = list(map(int, input().split()))
    s = [list(map(int, input().split())) for i in range(d)]
    #s[3][25] =   contest(25+1) of day(3+1)
    return d, c, s

def evolution(d, c, s, ans):
    score_before = evaluateSatisfaction(d, c, s, ans)
    ans_after = copy.copy(ans)

    idx1 = random.randint(0,d-1)
    idx2 = random.randint(0,d-1)
    
    tmp = ans_after[idx1]
    ans_after[idx1] = ans_after[idx2]
    ans_after[idx2] = tmp

    score_after = evaluateSatisfaction(d,c,s,ans_after)

    if score_after > score_before:
        return ans_after
    else:
        return ans

if __name__ == "__main__":
    
    d, c, s = Input()
    
    #print("val =", evaluateSatisfaction(d, c, s, [1, 17, 13, 14, 13]))

    #calc start
    t1 = time.time()
    ans = [0 for i in range(d)]
    last = [-1 for i in range(26)]
    for i in range(d):
        evalValueList = [0 for j in range(26)]
        for j in range(26):
            evalValueList[j] = valuationFunction(d, c, s, j,i,last)

        max_idx = 0
        max = evalValueList[0]

        for j in range(26):
            if (max < evalValueList[j]):
                max_idx = j
                max = evalValueList[j]
        
        ans[i] = max_idx
        last[ans[i]] = i


    
    #ans = [1, 2, 3, 4, 5]
    t2 = time.time()
    while(float(t2-t1) < 1.0):
        ans = evolution(d, c, s, ans)
        #print("ans = ",evaluateSatisfaction(d,c,s,ans))
        t2 = time.time()
    for x in ans:
        print(x + 1)
    #print(evaluateSatisfaction(d,c,s,ans))