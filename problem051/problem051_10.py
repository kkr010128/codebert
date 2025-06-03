while True:
    H, W = map(int, input().split())
    if not(H or W):
        break
    for i in range(H):
        if i % 2:
            print('.#' * (W // 2) + '.' * (W % 2))
        else:
            print('#.' * (W // 2) + '#' * (W % 2))
    print()