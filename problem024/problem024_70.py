n, k = map(int, input().split())
w = []
for i in range(n):
    w.append(int(input()))

def check(p):
    i = 0
    for _ in range(k):
        wight = 0
        while wight+w[i] <= p:
            wight += w[i]
            i += 1
            if i == n:
                return n
    return i

if __name__ == '__main__':
    left = 0
    right = 100000 * 10000
    mid = 0
    while right - left > 1:
        mid = (left+right)//2
        v = check(mid)
        if v >= n:
            right = mid
        else:
            left = mid
    print(right)

