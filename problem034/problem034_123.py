# coding=utf-8


class Dice(object):

    def __init__(self, label):
        self.label = label

    def _rotateS(self):
        s1, s2, s3, s4, s5, s6 = self.label
        self.label = [s5, s1, s3, s4, s6, s2]

    def _rotateN(self):
        s1, s2, s3, s4, s5, s6 = self.label
        self.label = [s2, s6, s3, s4, s1, s5]

    def _rotateE(self):
        s1, s2, s3, s4, s5, s6 = self.label
        self.label = [s4, s2, s1, s6, s5, s3]

    def _rotateW(self):
        s1, s2, s3, s4, s5, s6 = self.label
        self.label = [s3, s2, s6, s1, s5, s4]

    def _spinPos(self):
        s1, s2, s3, s4, s5, s6 = self.label
        self.label = [s1, s4, s2, s5, s3, s6]

    def _spinNeg(self):
        s1, s2, s3, s4, s5, s6 = self.label
        self.label = [s1, s3, s5, s2, s4, s6]

    def rotate(self, r):
        if r == 'S':
            self._rotateS()
        elif r == 'N':
            self._rotateN()
        elif r == 'E':
            self._rotateE()
        elif r == 'W':
            self._rotateW()
        elif r == 'SP':
            self._spinPos()
        elif r == 'SN':
            self._spinNeg()
        elif r == '2S':
            self._rotateS()
            self._rotateS()
        elif r == '2SP':
            self._spinPos()
            self._spinPos()

    def getLabel(self, i):
        return self.label[i - 1]

    def match(self, top, front):
        iTop = self.label.index(top) + 1
        topRot = {1: '', 2: 'N', 3: 'W', 4: 'E', 5: 'S', 6: '2S'}
        self.rotate(topRot[iTop])

        iFront = self.label.index(front) + 1
        frontRot = {2: '', 3: 'SN', 4: 'SP', 5: '2SP'}
        self.rotate(frontRot[iFront])


def main():
    d = Dice(map(int, raw_input().split()))
    n = input()
    for _ in xrange(n):
        top, front = map(int, raw_input().split())
        d.match(top, front)
        print d.getLabel(3)

if __name__ == '__main__':
    main()