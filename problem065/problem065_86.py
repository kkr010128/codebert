# coding:utf-8
W = raw_input().lower()
array = []
cnt = 0
while True:
    line = raw_input()
    if line == "END_OF_TEXT":
        break
    split = line.lower().split()
    for s in split:
        array.append(s)
for word in array:
    if W == word:
        cnt += 1
print cnt

