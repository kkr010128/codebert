def main():
    D = int(input())
    C = [0] * 26
    C = list(map(int,input().split()))
    S = [ list(map(int,input().split(" "))) for i in range(D)]
    
    score = 0
    last = [0] * 26
    for i in range(D):
        t = int(input())
        for j in range(26):
            if j+1 == t:
                last[j] = 0
                score += S[i][j]
            else:
                last[j] += 1
                score -= last[j]*C[j]
        print(score)
if __name__ == '__main__':
    main()