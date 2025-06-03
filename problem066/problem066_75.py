def shuffle():
    h = int(input())
    for i in range(h):
        s.append(s[0])
        del s[0]


while True:
    s = list(input())
    if s == ['-']:
        break
    m = int(input())
    for i in range(m):
        shuffle()
    print(''.join(s))
