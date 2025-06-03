W = input()

T = ""
while True:
    x = input()
    if x == "END_OF_TEXT":
        break
    T += x + " "

num = 0
for t in T.split():
    if t.lower() == W.lower():
        num += 1

print(num)