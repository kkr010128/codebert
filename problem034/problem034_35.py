class Dice:
    # constructor
    def __init__(self, eye1, eye2, eye3, eye4, eye5, eye6):
        self.__eyes = {
            "top": eye1,
            "front": eye2,
            "right": eye3,
            "left": eye4,
            "back": eye5,
            "bottom": eye6
        }
    # setter
    def set_eyes(self, eye1, eye2, eye3, eye4, eye5, eye6):
        self.__eyes["top"] = eye1
        self.__eyes["front"] = eye2
        self.__eyes["right"] = eye3
        self.__eyes["left"] = eye4
        self.__eyes["back"] = eye5
        self.__eyes["bottom"] = eye6
    # getter
    def get_eyes(self, key):
        return self.__eyes[key]

    
    def N(self):
        self.set_eyes(
            self.get_eyes("front"),
            self.get_eyes("bottom"),
            self.get_eyes("right"),
            self.get_eyes("left"),
            self.get_eyes("top"),
            self.get_eyes("back")
            )
    def S(self):
        self.set_eyes(
            self.get_eyes("back"),
            self.get_eyes("top"),
            self.get_eyes("right"),
            self.get_eyes("left"),
            self.get_eyes("bottom"),
            self.get_eyes("front")
            )
        
    def E(self):
        self.set_eyes(
            self.get_eyes("left"),
            self.get_eyes("front"),
            self.get_eyes("top"),
            self.get_eyes("bottom"),
            self.get_eyes("back"),
            self.get_eyes("right")
            )
        
    def W(self):
        self.set_eyes(
            self.get_eyes("right"),
            self.get_eyes("front"),
            self.get_eyes("bottom"),
            self.get_eyes("top"),
            self.get_eyes("back"),
            self.get_eyes("left")
            )
    
    def print_top(self):
        print(self.get_eyes("top"))
    

    def guess_right_from_top_front(self, top, front):
        key_top = None
        key_front = None
        keys = [ 
        "top", 
        "front", 
        "right", 
        "left", 
        "back", 
        "bottom"
        ]
        for key in keys:
            if top == self.get_eyes(key):
                key_top = key
            if front == self.get_eyes(key):
                key_front = key
        keys_for_top = [
            ["front", "right", "back", "left"],
            ["bottom", "right", "top", "left"],
            ["bottom", "back", "top", "front"],
            ["bottom", "front", "top", "back"],
            ["bottom", "left", "top", "right"],
            ["front", "left", "back", "right"]
        ]
        
        for i in range(6):
            if key_top == keys[i]:
                for j in range(4):
                    if key_front == keys_for_top[i][j]:
                        return keys_for_top[i][(j + 1) % 4]

eye1, eye2, eye3, eye4, eye5, eye6 = map(int, input().split())
q = int(input())
dice = Dice(eye1, eye2, eye3, eye4, eye5, eye6)
for _ in range(q):
    top, front = map(int, input().split())
    print(dice.get_eyes(dice.guess_right_from_top_front(top, front)))

