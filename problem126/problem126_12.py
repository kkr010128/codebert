a = input()
b = a.split(" ")
for i in range(len(b)):
    if b[i] == "0":
        print(i + 1)
        break
