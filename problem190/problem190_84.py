def main():
    S = str(input())
    n = len(S)
    frontN = (n - 1) // 2
    backN = (n + 3) // 2
    
    checkFN = frontN // 2
    checkFNW = S[0:frontN]
    for i in range(checkFN):
        temp = (i + 1) * -1
        if checkFNW[i] == checkFNW[temp]:
            continue
        else:
            print('No')
            return
    
    checkBN = n - backN
    checkBNW = S[backN - 1:n]
    for i in range(checkBN // 2):
        temp = (i + 1) * -1
        if checkBNW[i] == checkBNW[temp]:
            continue
        else:
            print('No')
            return

    for i in range(n // 2):
        temp = (i + 1) * -1
        if S[i] == S[temp]:
            continue
        else:
            print('No')
            return
    
    print('Yes')
main()