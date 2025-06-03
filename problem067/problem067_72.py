n = int(raw_input())
tp = 0; hp = 0
for i in range(n):
    tw,hw = raw_input().split()
    if tw == hw:
        tp += 1
        hp += 1
    elif tw > hw:
        tp += 3
    elif tw < hw:
        hp += 3
print '%s %s' % (tp,hp)