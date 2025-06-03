l = 'abcdefghijklmnopqrstuvwxyz'
mp = [0 for _ in list(l)]

while True:
    try:
        in_data = list(filter(lambda x: 97 <= ord(x) <= 122 , raw_input().lower()))
    except:
        break

    for s in in_data:
        mp[ord(s) - 97] += 1

for i,j in zip(l, mp):
    print "%s : %s" % (i, j)