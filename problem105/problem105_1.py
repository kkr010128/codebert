def solve(N, a):
    count = 0
    for i in range(1,N+1):
        if i % 2 == 1 and a[i] % 2 ==1:
            count += 1
    return count
N = int(input())
a = [0] + list(map(int, input().split()))
print(solve(N, a))