import sys

def solve():
    input = sys.stdin.readline
    S = list(input().strip("\n"))
    K = int(input())
    N = len(S)
    head, tail, joint = 0, 0, 0
    inside = 0
    if S[0] == S[N-1]: #ジョイント部を考える必要がある場合
        isInitial = True
        current = S[0]
        currentLength = 1
        for i in range(1, N):
            if S[i] == current: currentLength += 1
            else:
                if isInitial: 
                    head = currentLength // 2
                    isInitial = False
                else: inside += currentLength // 2
                current = S[i]
                currentLength = 1
        if isInitial: #全て同じ文字の場合
            totalLength = N * K
            print(totalLength // 2)
        else:
            tail = currentLength // 2
            for i in range(N):
                if S[i] == current: currentLength += 1
                else: 
                    joint = currentLength // 2
                    break
            print(head + tail + joint * (K - 1) + inside * K)
    else:
        current = S[0]
        currentLength = 1
        for i in range(1, N):
            if S[i] == current: currentLength += 1
            else:
                inside += currentLength // 2
                current = S[i]
                currentLength = 1
        inside += currentLength // 2
        print(inside * K)   
    #print(head, tail, joint, inside)        
    return 0

if __name__ == "__main__":
    solve()