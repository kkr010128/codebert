def solve():
    N = int(input())
    S = input()
    C = [c for c in S]

    left = 0
    right = len(C) -1
    ans = 0
    while left < right:
        while left < right and C[left] == 'R':
            left += 1
        while left < right and C[right] == 'W':
            right -= 1
        if left < right:
            C[left] = 'R'
            C[right] = 'W'
            ans += 1
            left += 1
            right -= 1
    print(ans)

if __name__ == "__main__":
    solve()