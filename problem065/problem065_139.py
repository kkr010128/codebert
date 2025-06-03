w = input().lower()
t = ""
while True:
    tmp = input()
    t += " "+tmp.lower()
    if tmp=="END_OF_TEXT":
        break
t=t.split()
print(t.count(w))