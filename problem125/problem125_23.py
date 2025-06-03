# -*- coding: utf-8 -*-
moji=[]
moji.append("eraser")
moji.append("erase")
moji.append("dreamer")
moji.append("dream")
user = "erasedream"
user = int(input())
result = user
count = 1

while result != 0:
    result += user
    result %= 360
    count += 1
print(count,end="")
