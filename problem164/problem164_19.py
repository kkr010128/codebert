abcd = input().split()

hp1 = int(abcd[0])
at1 = int(abcd[1])
hp2 = int(abcd[2])
at2 = int(abcd[3])

while hp1 > 0 and hp2 > 0:
    hp2 -= at1
    if hp2 <= 0:
        print("Yes")
        break

    hp1 -= at2
    if hp1 <= 0:
        print("No")
        break