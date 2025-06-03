class Dice:
    def __init__(self):
        self.side = {"top": 0, "front": 0, "right": 0, "left": 0, "back": 0, "bottom": 0}

    # サイコロを東西南北、どちらか一方に転がした時、それぞれの面の変化
    def roll(self, direction):
        self.direction = direction
        if self.direction == "N":
            w = self.side["top"]
            self.side["top"] = self.side["front"]
            self.side["front"] = self.side["bottom"]
            self.side["bottom"] = self.side["back"]
            self.side["back"] = w
        elif self.direction == "S":
            w = self.side["top"]
            self.side["top"] = self.side["back"]
            self.side["back"] = self.side["bottom"]
            self.side["bottom"] = self.side["front"]
            self.side["front"] = w
        elif self.direction == "E":
            w = self.side["top"]
            self.side["top"] = self.side["left"]
            self.side["left"] = self.side["bottom"]
            self.side["bottom"] = self.side["right"]
            self.side["right"] = w
        elif self.direction == "W":
            w = self.side["top"]
            self.side["top"] = self.side["right"]
            self.side["right"] = self.side["bottom"]
            self.side["bottom"] = self.side["left"]
            self.side["left"] = w

    # サイコロの面の位置関係
    def position_relation(self, top, front):
        # 北に転がした場合
        if top == "top" and front == "front"\
        or top == "front" and front == "bottom"\
        or top == "bottom" and front == "back"\
        or top == "back" and front == "top":
            self.right = self.side["right"]
        # 北に転がした時の"top"と"front"を入れ替えた場合 
        if top == "top" and front == "back"\
        or top == "back" and front == "bottom"\
        or top == "bottom" and front == "front"\
        or top == "front" and front == "top":
            self.right = self.side["left"]
        # 東に転がした場合
        if top == "top" and front == "right"\
        or top == "right" and front == "bottom"\
        or top == "bottom" and front == "left"\
        or top == "left" and front == "top":
            self.right = self.side["back"]
        # 東に転がした時の"top"と"front"を入れ替えた場合
        if top == "top" and front == "left"\
        or top == "left" and front == "bottom"\
        or top == "bottom" and front == "right"\
        or top == "right" and front == "top":
            self.right = self.side["front"]
        # 西に転がした場合
        if top == "front" and front == "right"\
        or top == "right" and front == "back"\
        or top == "back" and front == "left"\
        or top == "left" and front == "front":
            self.right = self.side["top"]
        # 西に転がした時の"top"と"front"を入れ替えた場合
        if top == "front" and front == "left"\
        or top == "left" and front == "back"\
        or top == "back" and front == "right"\
        or top == "right" and front == "front":
            self.right = self.side["bottom"]

dice = Dice()
for s, n in zip(dice.side, input().split()):
    dice.side[s] = int(n)

q = int(input())
for i in range(q):
    t, f = map(int, input().split())
    for k, v in dice.side.items():
        if t == v:
            top = k
        if f == v:
            front = k
    dice.position_relation(top, front)
    print(dice.right)

