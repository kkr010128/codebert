combined = input().split(" ")
s = int(combined[0])
w = int(combined[1])

if w >= s:
    print("unsafe")
else:
    print("safe")
