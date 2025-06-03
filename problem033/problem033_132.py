import copy

class Dice:
    def __init__(self, numbers):
        self.dd = dict(zip(['U', 'S', 'E', 'W', 'N', 'B'], numbers))

    def next(self, o):
        old = copy.deepcopy(self.dd)
        if o == 'E':
            self.dd['B'] = old['E']
            self.dd['U'] = old['W']
            self.dd['E'] = old['U']
            self.dd['W'] = old['B']
        elif o == 'S':
            self.dd['B'] = old['S']
            self.dd['U'] = old['N']
            self.dd['S'] = old['U']
            self.dd['N'] = old['B']
        elif o == 'W':
            self.dd['B'] = old['W']
            self.dd['U'] = old['E']
            self.dd['E'] = old['B']
            self.dd['W'] = old['U']
        elif o == 'N':
            self.dd['B'] = old['N']
            self.dd['U'] = old['S']
            self.dd['S'] = old['B']
            self.dd['N'] = old['U']

dn = [int(n) for n in input().split()]
op = input()
ad = Dice(dn)

for o in op:
    ad.next(o)

print(ad.dd['U'])