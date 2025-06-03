class Battle:
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

    def result(self):
        while self.A > 0 or self.C > 0:
            self.C -= self.B
            if self.C <= 0:
                return "Yes"
            self.A -= self.D
            if self.A <= 0:
                return "No"


def atc_164b(ABCD: str) -> str:
    A, B, C, D = map(int, ABCD.split(" "))
    battle = Battle(A, B, C, D)
    return battle.result()


ABCD_input = input()
print(atc_164b(ABCD_input))
