def main():
    r, c = map(int, input().split())
    table = []
    for _ in range(r):
        table.append(list(map(int, input().split())))
    table.append([0] * (c+1))
    for index, line in enumerate(table[:-1]):
        table[index].append(sum(line))
        for index1, value in enumerate(table[index]):
            table[-1][index1] += value
    for line in [map(str, line) for line in table]:
        print(' '.join(line))
    return


if __name__ == '__main__':
    main()

