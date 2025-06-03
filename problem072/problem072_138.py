

def main():
    N = int(input())
    zoro = []

    for i in range(N):
        a, b = map(int, input().split())
        if a == b:
            zoro.append(1)
            if i >= 2:
                if zoro[i-2] == zoro[i-1] and zoro[i-1] == zoro[i]:
                    print('Yes')
                    return
        else:
            zoro.append(0)

    print('No')


main()
