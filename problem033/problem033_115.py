# coding=utf-8


class Dice(object):

    def __init__(self, label):
        self.label = label

    def rotateS(self):
        s1, s2, s3, s4, s5, s6 = self.label
        self.label = [s5, s1, s3, s4, s6, s2]

    def rotateN(self):
        s1, s2, s3, s4, s5, s6 = self.label
        self.label = [s2, s6, s3, s4, s1, s5]

    def rotateE(self):
        s1, s2, s3, s4, s5, s6 = self.label
        self.label = [s4, s2, s1, s6, s5, s3]

    def rotateW(self):
        s1, s2, s3, s4, s5, s6 = self.label
        self.label = [s3, s2, s6, s1, s5, s4]

    def rotate(self, r):
        if r == 'S':
            self.rotateS()
        elif r == 'N':
            self.rotateN()
        elif r == 'E':
            self.rotateE()
        elif r == 'W':
            self.rotateW()
        else:
            print 'Cannot rotate into ' + r + 'direction.'

    def getTopLabel(self):
        return self.label[0]


if __name__ == '__main__':
    d = Dice(map(int, raw_input().split()))
    rotations = raw_input()
    for r in rotations:
        d.rotate(r)
    print d.getTopLabel()