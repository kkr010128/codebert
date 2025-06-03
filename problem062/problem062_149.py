while True:
    table=str(input())
    if table[0] == '0':
        break
    print(sum(int(num) for num in(table)))

