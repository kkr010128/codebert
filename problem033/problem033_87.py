label = input().split()
rot = input()
 
dice = {
        "top":1,
        "front":2,
        "right":3,
        "left":4,
        "back":5,
        "bottom":6
        }
 
for r in rot:
    if r == 'E':
        dice["top"], dice["left"], dice["bottom"], dice["right"] = \
        dice["left"], dice["bottom"], dice["right"], dice["top"]
    elif r == 'N':
        dice["top"], dice["front"], dice["bottom"], dice["back"] = \
        dice["front"], dice["bottom"], dice["back"], dice["top"]
    elif r == 'S':
        dice["top"], dice["back"], dice["bottom"], dice["front"] = \
        dice["back"], dice["bottom"], dice["front"], dice["top"]
    elif r == 'W':
        dice["top"], dice["right"], dice["bottom"], dice["left"] = \
        dice["right"], dice["bottom"], dice["left"], dice["top"]
print(label[dice["top"]-1])