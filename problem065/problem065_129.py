t = []
w = input().lower()
while True:
    s = input()
    if s == "END_OF_TEXT":
        break
    t.extend(s.lower().split())
print(t.count(w))
