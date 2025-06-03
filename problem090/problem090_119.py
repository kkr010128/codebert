w = input()

if w.count("R") == 2:
    if w[1] == "R":
        print(2)
    else:
        print(1)

else:
    print(w.count("R"))