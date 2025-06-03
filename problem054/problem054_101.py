Spades   = 0
Hearts   = 1
Clovers  = 2
Diamonds = 3
Cards = [[Spades, Hearts, Clovers, Diamonds] for j in range(13)]

for i in range(4):
    for j in range(13):
        Cards[j][i] = True

n = input()

for i in range(n):
    Input = raw_input().split()

    Numb = int(Input[1])
    if Input[0] == 'S':
        Mark = Spades
    if Input[0] == 'H':
        Mark = Hearts
    if Input[0] == 'C':
        Mark = Clovers
    if Input[0] == 'D':
        Mark = Diamonds

    Cards[Numb - 1][Mark] = False

for i in range(4):
    for j in range(13):
        if Cards[j][i]:
            if i == Spades:
                print 'S', j + 1
            if i == Hearts:
                print 'H', j + 1
            if i == Clovers:
                print 'C', j + 1
            if i == Diamonds:
                print 'D', j + 1