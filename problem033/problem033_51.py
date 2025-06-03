class diceClass:
    label = []
    def __init__(self,l):
        if len(l) == 6:
            self.label = l
    def move(self,c):
        if c.upper() == 'N':
            buf = []
            buf.append(self.label[1])
            buf.append(self.label[5])
            buf.append(self.label[2])
            buf.append(self.label[3])
            buf.append(self.label[0])
            buf.append(self.label[4])
            self.label = buf
        elif c.upper() == 'E':
            buf = []
            buf.append(self.label[3])
            buf.append(self.label[1])
            buf.append(self.label[0])
            buf.append(self.label[5])
            buf.append(self.label[4])
            buf.append(self.label[2])
            self.label = buf
        elif c.upper() == 'W':
            buf = []
            buf.append(self.label[2])
            buf.append(self.label[1])
            buf.append(self.label[5])
            buf.append(self.label[0])
            buf.append(self.label[4])
            buf.append(self.label[3])
            self.label = buf
        elif c.upper() == 'S':
            buf = []
            buf.append(self.label[4])
            buf.append(self.label[0])
            buf.append(self.label[2])
            buf.append(self.label[3])
            buf.append(self.label[5])
            buf.append(self.label[1])
            self.label = buf
    def get_label(self):
        return self.label[0]
in_line = raw_input().split()
dice = diceClass(in_line)
move = raw_input()
for c in move:
    dice.move(c)
print dice.get_label()