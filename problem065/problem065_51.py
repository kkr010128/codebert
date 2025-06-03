W = raw_input().lower()
doc = []
while True:
    tmp = raw_input()
    if tmp == 'END_OF_TEXT':
        break
    doc.extend(tmp.lower().split())
print doc.count(W)