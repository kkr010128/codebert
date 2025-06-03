W = input().casefold()
count=0
while True:
    line = input()
    if line == "END_OF_TEXT":
        break
    line = line.casefold()
    word = line.split()
    count += word.count(W)

print(count)