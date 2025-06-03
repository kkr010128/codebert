w = input().lower()
count = 0

while True:
    s = input()
    if s == "END_OF_TEXT":
        break
    count += s.lower().split().count(w)

print(count)