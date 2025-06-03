class Dice:
    def __init__(self, ary): # [top, front, right, left, back, bottom]
        self.__top = ary[0]
        self.__fro = ary[1]
        self.__rit = ary[2]
        self.__lft = ary[3]
        self.__bak = ary[4]
        self.__btm = ary[5]

    def turn_e(self): # 右に転がる
        self.__top, self.__lft, self.__btm, self.__rit = \
        self.__lft, self.__btm, self.__rit, self.__top

    def turn_s(self): # 手前に転がる
        self.__top, self.__fro, self.__btm, self.__bak = \
        self.__bak, self.__top, self.__fro, self.__btm

    def turn_w(self): # 左に転がる
        self.__top, self.__lft, self.__btm, self.__rit = \
        self.__rit, self.__top, self.__lft, self.__btm

    def turn_n(self): # 奥に転がる
        self.__top, self.__fro, self.__btm, self.__bak = \
        self.__fro, self.__btm, self.__bak, self.__top

    def spin_r(self): # 右回転 
        self.__rit, self.__fro, self.__lft, self.__bak = \
        self.__bak, self.__rit, self.__fro, self.__lft

    def spin_l(self): # 左回転
        self.__rit, self.__fro, self.__lft, self.__bak = \
        self.__fro, self.__lft, self.__bak, self.__rit

    def is_same_setting(self, ary): # 同じように置いているか
        if self.__top == ary[0] and self.__fro == ary[1] and self.__rit == ary[2] and \
            self.__lft == ary[3] and self.__bak == ary[4] and self.__btm == ary[5]:
            return True

    def is_same_dice(self, ary): # 回転させて同じダイスになるか
        is_same = False
        for _ in range(2):
            for _ in range(3):
                for _ in range(4):
                    if self.is_same_setting(ary):
                        is_same = True
                    self.spin_r()
                self.turn_n()
            self.spin_r()
            self.turn_s()
        return is_same

    def show_top(self): # 上面の値を表示
        return self.__top

surfaces = list(map(int,input().split()))
instructions = list(input())

dice = Dice(surfaces)

for inst in instructions:
    if inst == "E":
        dice.turn_e()
    if inst == "N":
        dice.turn_n()
    if inst == "S":
        dice.turn_s()
    if inst == "W":
        dice.turn_w()

print(dice.show_top())
