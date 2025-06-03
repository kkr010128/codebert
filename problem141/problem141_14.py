import math

ceil = math.ceil

def main(N, A):
    A.reverse()
    pos = [(A[0], A[0])]
    for i in range(len(A)-1):
        tmpmin = ceil(pos[-1][0]/2) + A[i+1]
        tmpmax = pos[-1][1] + A[i+1]
        pos.append((tmpmin, tmpmax))

    l,r = pos.pop()
    if l > 1:
        return -1
    
    ki = [1]
    A.reverse()
    for j in range(N):
        m = (ki[j]-A[j])*2
        l, r = pos.pop()
        if m < l:
            return -1
        ki.append(min(r, m))
    
    return sum(ki)

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    ans = main(N, A)
    print(ans)
