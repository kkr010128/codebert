def is_kaibun(string):
    isk = True
    length = len(string)
    for i in range(length // 2):
        if string[i] != string[length - 1 - i]:
            isk = False
            break
    return isk

s = input()
len_s = len(s)
if is_kaibun(s[0:(len_s // 2)]) and is_kaibun(s):
    print('Yes')
else:
    print('No')
