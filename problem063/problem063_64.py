s = ""
while True:
    try:
        s += input().lower()
    except:
        break

for c in [chr(i) for i in range(ord('a'), ord('z') + 1)]:
    print(c, ":", s.count(c))