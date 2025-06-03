out = 0

inp = list(map(int, input().split()))

while 0<len(inp):
    out += inp.pop(0)

if out <= 21:
    print('win')
else:
    print('bust')