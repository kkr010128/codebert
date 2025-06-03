n, k = (int(i) for i in input().split())
w = [int(input()) for i in range(n)]

total_weght = sum(w)

def check(p):
    track = [0 for i in range(k)]
    target = 0

    for i in range(k):
        while (track[i] + w[target]) <= p:
            track[i] += w[target]
            target += 1
            if target not in range(n):
                break
        if target not in range(n):
            break
    
    return(target)

def solve(n):
    left = 0
    right = 100000 * 100000
    while left < right:
        
        mid = (left + right) // 2
        if n == check(mid):
            right = mid
        else:
            left = mid + 1

    return(right)

if __name__ == "__main__":
    ans = solve(n)
    print(ans)

