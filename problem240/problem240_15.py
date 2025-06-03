import numpy as np

def solve():
    dp = np.zeros((2, N+1))
#    print(dp)
    ac = 0
    wa = 0
    for i in range(M): 
        if (dp[0][S[i][0]] == 0):
            if(S[i][1] == "WA"):
                dp[1][S[i][0]] += 1
            elif(S[i][1] == "AC"):
                ac += 1
                dp[0][S[i][0]] = 1
                wa += dp[1][S[i][0]]
    print(ac, int(wa))

if __name__=="__main__":

    N, M = list(map(int, input().split()))
    S = []
    for i in range(M):
        a,b = input().split()
        S.append([int(a), b])
#    print(S)
    solve()
    


