word = input()
text = []
count = 0

while True:
    x = input()
    if x == "END_OF_TEXT":
        break
    x = x.split()
    for i in x:
        if i.lower() == word:
            count += 1

print(count)
