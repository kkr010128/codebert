def main():
    D = int(input())
    C = [0] * 26
    C = list(map(int,input().split()))
    S = [ list(map(int,input().split(" "))) for i in range(D)]
    
    last = [0] * 26
    for i in range(D):
        max = -9999999999999
        max_t = 0
        for t in range(26):
            score = 0
            for j in range(26):
                if j == t:
                    #last[j] = 0
                    score += S[i][j]
                else:
                    #last[j] += 1
                    score -= (last[j]+10)*C[j]
            if  score > max:
                max = score
                max_t = t
        for j in range(26):
            if j == max_t:
                last[j] = 0
            else:
                last[j] += 1
        print(max_t + 1)
if __name__ == '__main__':
    main()