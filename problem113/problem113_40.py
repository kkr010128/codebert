import random
import time
import copy

def down_score(d, c, last_d, score):
    sum = 0
    for i in range(26):
        sum = sum + c[i]*(d-last_d[i])
        
    return int(score - sum)


def main():
    D = int(input())

    c = list(map(int, input().split()))

    s = [list(map(int, input().split())) for i in range(D)]

    start = time.time()
    
    last_d = [0 for i in range(26)]
    ans = []    
    score1 = 0
    
    for i in range(D):
        max = 0
        idx = 0
        for j in range(26):
            if max < (s[i][j] + c[j] * (i-last_d[j])*(i-last_d[j]+1)/2) and c[j] != 0:
                max = s[i][j] + c[j] * (i-last_d[j])*(i-last_d[j]+1)/2
                idx = j
            elif max == (s[i][j] + c[j] * (i-last_d[j])*(i-last_d[j]+1)/2) and c[j] * (i-last_d[j])*(i-last_d[j]+1)/2 > c[idx]* (i-last_d[idx])*(i-last_d[idx]+1)/2 and c[j] != 0:
                idx = j
            
        last_d[idx] = i+1
        score1 += s[i][idx]
        score1 = down_score(i+1,c,last_d,score1)
        
        ans.append(idx)

    while time.time() - start < 1.9:
        cp = ans.copy()
        last_d = [0 for i in range(26)]
        score2 = 0  
        
        idx1 = random.randint(0,25)
        idx2 = random.randint(0,25)
        idx3 = random.randint(0,25)
        if random.randint(0,1):
            d1 = random.randint(0,D-1) 
            d2 = random.randint(0,D-1)
            d3 = random.randint(0,D-1)
            if idx1 == idx2 or idx1 == idx3 or idx2 == idx3:
                continue
            if random.randint(0,1):
                ans[d1] = idx1
            elif random.randint(0,1):
                ans[d1] = idx1
                ans[d2] = idx2
            else:
                ans[d1] = idx1
                ans[d2] = idx2
                ans[d3] = idx3
                                
        #2値入れ替え
        elif random.randint(0,1):           
            d1 = random.randint(0,D-8) 
            d2 = random.randint(d1+1,d1+7)
            tmp1 = ans[d1]
            tmp2 = ans[d2]
            if random.randint(0,1):
                ans[d1] = tmp2
                ans[d2] = tmp1
            
        #3値入れ替え          
        else:
            d1 = random.randint(0,D-11) 
            d2 = random.randint(d1+1,d1+5)
            d3 = random.randint(d2+1,d2+5) 
            tmp1 = ans[d1]
            tmp2 = ans[d2]
            tmp3 = ans[d3]
            if random.randint(0,1):
                ans[d1] = tmp2
                ans[d2] = tmp3
                ans[d3] = tmp1
            else:
                ans[d1] = tmp3
                ans[d2] = tmp1
                ans[d3] = tmp2
            
        for i in range(D):
            score2 += s[i][ans[i]]
            last_d[ans[i]] = i+1
            score2 = down_score(i+1, c, last_d, score2)
        
        if score1 > score2:
            ans = cp.copy()
        else:
            score1 = score2
    
    for i in range(D):
        print(ans[i]+1)  

if __name__ == "__main__":
    main()
