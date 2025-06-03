def main():
    """"ここに今までのコード"""
    N, K = map(int, input().split())
    dice_list = list(map(int, input().split()))
    max, s = 0, 0

    for i in range(K):
        s += (dice_list[i] + 1) / 2
    
    max = s

    for i in range(N-K):
        s -= (dice_list[i] + 1) / 2
        s += (dice_list[i+K] + 1) / 2
        if s > max:
            max = s
    
    print(max)


if __name__ == '__main__':
    main()