x = input()
window = int(x.split()[0])
b = int(x.split()[1])
curtain = b * 2

if window > curtain:
    print(window - curtain)
else:
    print('0')