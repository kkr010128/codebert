class MyClass():
    def main(self):
        self.n = input()
        self.A = map(int,raw_input().split())
        self.q = input()
        self.M = map(int,raw_input().split())
        
        W = map(self.solve,self.M)
        for w in W:
            print w

    def solve(self,m):
        w = self.rec(m,self.A)
        if w:
            return "yes"
        else:
            return "no"

    def rec(self,m,A):
        if len(A) == 1:
            r1 = False
        else:
            r1 = self.rec(m,A[1:])

        m_new = m - A[0]
        if m_new == 0:
            r2 = True
        elif len(A) > 1 and min(A[1:]) <= m_new <= sum(A[1:]):
            r2 = self.rec(m_new,A[1:])
        else:
            r2 = False

        if r1 or r2:
            return True
        else:
            return False

if __name__ == "__main__":
    MC = MyClass()
    MC.main()