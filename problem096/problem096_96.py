import numpy as np

def main(Z, D):
    lengthes = np.linalg.norm(Z, axis=1)
    ans = np.sum(lengthes<=D)
    return ans

if __name__ == '__main__':
    N, D = map(int, input().split())
    Z = np.zeros([N, 2])
    for i in range(N):
        X, Y = map(int, input().split())
        Z[i][0] = X
        Z[i][1] = Y
    #print(Z)
    ans = main(Z, D)
    print(ans)

