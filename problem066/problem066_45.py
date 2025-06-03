while True:
    C = input()
    if C == "-":
        break
    count = int(input())
    shuffle = [int(input()) for i in range(count)]
    for h in shuffle:
        C = C[h:] + C[:h]
    print(C)