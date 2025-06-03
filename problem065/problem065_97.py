w = input().casefold()
c = 0
while True:
    _ = input()
    if(_ == "END_OF_TEXT"):
        break
    t = _.casefold().split()
    c += t.count(w)

print(c)