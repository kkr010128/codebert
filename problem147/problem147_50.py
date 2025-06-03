S = input()
T = input()

for i in range(ord('a'), ord('z') + 1):
    if T == S + chr(i):
        print("Yes")
        break
else:
    print("No")