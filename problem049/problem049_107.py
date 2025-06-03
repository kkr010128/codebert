while True:
    H, W = map(int, input().split())
    if not(H or W):
        break
    print(('#' * W + '\n') * H)