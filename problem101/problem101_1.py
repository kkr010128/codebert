def main(A,B,C,K):
    ans=False
    while K >= 0:
        if A < B:
            if B < C:
                ans=True
                return ans
            else:
                C = C * 2
        else:
            B = B * 2
        K=K-1
    return ans
A,B,C=map(int, input().split())
K=int(input())
ans=main(A,B,C,K)
print('Yes' if ans else 'No')