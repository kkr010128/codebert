

c = input()



ls = [chr(ord('a') + i) for i in range(26)]

for i in range(len(ls)):
    if ls[i] == c:
        print(ls[i + 1])
        break

