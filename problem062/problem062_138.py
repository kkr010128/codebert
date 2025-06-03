while True:
    instr = input()

    if instr == '0':
        break

    total = 0
    for s in instr:
        total += int(s)

    print(total)

