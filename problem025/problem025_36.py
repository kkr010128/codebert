class Solver():
    def __init__(self, A: [int]):
        self.A = A
        self.max_depth = len(A)

    def solve(self, tgt):
        self.tgt = tgt
        self.history = (self.max_depth+1)*[4000 * [None]]
        self.history = [[None for i in range(4000)] for x in range(self.max_depth + 1)]
        if self._rec_solve(0, 0):
            return 'yes'
        else:
            return 'no'

    def _rec_solve(self, _sum, index):
        if self.history[index][_sum] is not None:
            return self.history[index][_sum]
        if _sum == self.tgt:
            self.history[index][_sum] = True
            return True
        if index >= self.max_depth or _sum > self.tgt:
            self.history[index][_sum] = False
            return False
        self.history[index][_sum] = self._rec_solve(_sum + self.A[index], index + 1) or self._rec_solve(_sum, index + 1)
        return self.history[index][_sum]
            


if __name__ == '__main__':
    n = int(input())
    A = [int(i) for i in input().rstrip().split()]
    q = int(input())
    m_ary = [int(i) for i in input().rstrip().split()]
    s = Solver(A)
    for val in m_ary:
        print(s.solve(val))