def solve():
    N,M = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    total = sum(A)
    threshold = float(total) / (4*M)
    cnt = 0
    for num in A:
        if num >= threshold:
            cnt += 1
    if cnt >= M:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solve()