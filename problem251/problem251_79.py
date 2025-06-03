MOD = 10**9+7
def resolve():
    N, K = list(map(int, input().split()))
    R, S, P = list(map(int, input().split()))
    T = list(input())
    
    score = 0
    hands = {
        "r": ("p", P),
        "s": ("r", R),
        "p": ("s", S)
    }
    hist = []
    for i, t in enumerate(T):
        hand, point = hands[t]
        if i >= K and hand == hist[-K]:
            hist.append("*")
            continue
        score += point
        hist.append(hand)
    #print(hist)
    print(score)
    

if '__main__' == __name__:
    resolve()