Adr = [[[0 for r in range(10)]for f in range(3)]for b in range(4)]

n = input()

for i in range(n):
    Inf = map(int, raw_input().split())

    Adr[Inf[0]-1][Inf[1]-1][Inf[2]-1] += Inf[3]

for b in range(4):
    for f in range(3):
        print "",
        for r in range(10):
            if r != 9:
                print Adr[b][f][r],
            if r == 9:
                if f == 3:
                    print Adr[b][f][r],
                if f != 3:
                    print Adr[b][f][r]


    if b < 3:
        print "####################"