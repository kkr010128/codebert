def check(p):
    i = 0
    for j in range(track):
        s = 0
        while s + A[i] <= p:
            s += A[i]
            i += 1
            if i == budget:
                return True
    return False
    
def solve():
    left = max(A)
    right = sum(A)
    while (right - left > 1):
        mid = int((left + right) / 2)
        if check(mid):
            right = mid
        else :
            left = mid
    if check(left):
        return left
    else :
        return right

if __name__ == '__main__':
    budget, track = list(map(int, input().split()))
    A = []
    for n in range(budget):
        A.append(int(input()))     
    ans = solve()
    print(ans)
