S = input()

#print(S.count("R"))

con = S.count("R")

if con == 1:
    print(1)

elif con == 3:
    print(3)

elif con == 2:
    for j in range(3):
        if S[j] =="R":
            if S[j+1] =="R":
                print(2)
                break

            else:
                print(1)
                break

elif con == 0:
    print(0)
