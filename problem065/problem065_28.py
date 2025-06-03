W = input()
counter = 0
T = []
while True:
    string = input()
    if string == "END_OF_TEXT":
        break
    else:
        T.append(string)
for i in range(len(T)):
    memo = T[i].split()
    for j in range(len(memo)):
        if memo[j].lower() == W:
            counter += 1
print(counter)