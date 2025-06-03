w = int(input())
h = w // 3600
m = (w % 3600) // 60
s = w % 60
print(f"{h}:{m}:{s}")
