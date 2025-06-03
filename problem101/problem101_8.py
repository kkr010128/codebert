def solve(a, b, c, k):
    for i_a in range(k+1):
        for i_b in range(k+1):
            for i_c in range(k+1):
                if i_a + i_b + i_c > k:
                    break
                x = a * (2**i_a)
                y = b * (2**i_b)
                z = c * (2**i_c)
                if x < y < z:
                    return "Yes"
    return "No"

a, b, c = map(int, input().split())
k = int(input())
print(solve(a, b, c, k))