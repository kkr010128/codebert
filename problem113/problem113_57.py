import random

def down_score(d, c, last_d, score):
    sum = 0
    for i in range(26):
        sum += c[i]*(d-last_d[i])
        
    return (score - sum)

def main():
    D = int(input())

    c = list(map(int, input().split()))

    s = [list(map(int, input().split())) for i in range(D)]

    #print(c)

    #print(s)

    last_d = [0 for i in range(26)]
    
    ans = []
    
    score = 0
    
    for i in range(D):
        max = 0
        idx = 0
        for j in range(26):
            if max < (s[i][j] + c[j] * (i-last_d[j])*(i-last_d[j]+1)/2) and c[j] != 0:
                max = s[i][j] + c[j] * (i-last_d[j])*(i-last_d[j]+1)/2
                idx = j
            elif max == (s[i][j] + c[j] * (i-last_d[j])*(i-last_d[j]+1)/2) and c[j] * (i-last_d[j])*(i-last_d[j]+1)/2 > c[idx]* (i-last_d[idx])*(i-last_d[idx]+1)/2 and i-last_d[j]>i-last_d[idx]:
                idx = j
        last_d[idx] = i+1
        score += s[i][j]
        down_score(i+1,c,last_d,score)
        
        ans.append(idx)

    for i in range(D):
        print(ans[i]+1)

if __name__ == "__main__":
    main()