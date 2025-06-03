line = input()
a, b = line.split(" ")
a = int(a)
b = int(b)

if a <= (b * 2):
    print(0)
elif a > (b*2):
    print(a-(b*2))
