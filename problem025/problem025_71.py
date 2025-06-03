import time

def sum_A(A, n):
    dic = {}
    #A_ = A
    #n_ = n
    
    def solve(i, m):
        if (i, m) in dic:
            return dic[(i, m)]
        if m == 0:
            dic[(i, m)] = True
        elif i >= n:
            dic[(i, m)] = False
        elif solve(i+1, m):
            dic[(i, m)] = True
        elif solve(i+1, m-A[i]):
            dic[(i, m)] = True
        else:
            dic[(i, m)] = False
        return dic[(i, m)]
    
    return solve

if __name__ == '__main__':
    n = int(raw_input())
    A = map(int, raw_input().split())
    q = int(raw_input())
    m = map(int, raw_input().split())

    #A = sorted(A)
    start = time.time()
    solve = sum_A(A, n)
    for m_i in m:
        print "yes" if solve(0, m_i) else "no"
    end = time.time()
    #print end - start