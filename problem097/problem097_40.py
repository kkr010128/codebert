Kin = int(input())

i = 0
now = 0

if (0 == (Kin % 2)) or (0 == (Kin % 5)):
    print(-1)
else:
    while 1:
        now = (now * 10 + 7) % Kin
        i+=1

        if now == 0:
            break
    print(i)