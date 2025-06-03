#!/usr/bin/env python3

def solve(x):
    if x >= 2000:
        return True
    memo = [True] + [False]*x

    def dp(k):
        if k == 0:
            return True
        for i in range(100,106):
            if k-i >= 0 and memo[k-i]:
                return True
        
        return False
    
    for i in range(x):
        memo[i+1] = dp(i+1)
    return memo[x]



def main():
    X = int(input())
    print(int(solve(X)))
    return

if __name__ == '__main__':
    main()
