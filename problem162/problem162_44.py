def e_rotation_matching():
    N, M = [int(i) for i in input().split()]

    if N % 2 == 1:
        ans = [(left, N - left) for left in range(1, (N // 2) + 1)]
    else:
        ans = []
        flag = False
        left, right = 1, N - 1
        while left < right:
            if not flag and right - left <= N // 2:
                right -= 1
                flag = True
            ans.append((left, right))
            left += 1
            right -= 1
    return '\n'.join([f'{a} {b}' for a, b in ans[:M]])

print(e_rotation_matching())