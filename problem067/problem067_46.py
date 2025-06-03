def card_game(pairs):
    points = [0, 0]
    for pair in pairs:
        if (pair[0] > pair[1]):
            points[0] += 3
        elif (pair[0] < pair[1]):
            points[1] += 3
        else:
            points[0] += 1
            points[1] += 1

    return points

if __name__ == '__main__':
    n = int(input())
    pairs = []
    for _ in range(n):
        pairs.append(input().split())

    points = card_game(pairs)
    print(' '.join(map(str, points)))

