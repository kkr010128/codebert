text = []
try:
    while True:
        text.append(input())
except:
    for s in [chr(k) for k in range(97,97+26)]:
        count = 0
        for i in text:
            count += i.lower().count(s)
        print(s,":",count)