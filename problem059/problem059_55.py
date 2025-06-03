def main():

    r,c = map(int, input().split())
    chart = [list(map(int, input().split())) for i in range(r)]
    total = [0 for i in range(c)]

    for row in chart:
        print((' '.join(map(str, row))) + ' ' + str(sum(row)))
        total = [x + y for (x, y) in zip(total, row)]

    print((' '.join(map(str, total))) + ' ' + str(sum(total)))


main()