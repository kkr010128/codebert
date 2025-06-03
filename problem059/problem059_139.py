if __name__ == '__main__':
    from sys import stdin

    r, c = (int(n) for n in stdin.readline().split())

    table = []
    for _ in range(r):
        row = [int(n) for n in stdin.readline().split()]
        row.append(sum(row))

        print(" ".join(map(str, row)))
        table.append(row)
        
    sum_column = (sum(column) for column in zip(*table))
    print(" ".join(map(str, sum_column)))

