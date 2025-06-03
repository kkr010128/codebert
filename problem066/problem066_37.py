import re
array = []
lines = []
count = 0
while True:
    n = input()
    if n == "-":
        break
    array.append(n)
for i in range(len(array)):
    if re.compile("[a-z]").search(array[i]):
        fuck = i+1
        if count > 0:
            lines.append(stt)
        count += 1
        stt = array[i]
    else:
        if i == fuck:
            continue
        stt = stt[int(array[i]):len(stt)]+stt[0:int(array[i])]
        if i == len(array)-1:
            lines.append(stt)
for i in range(len(lines)):
    print(lines[i])