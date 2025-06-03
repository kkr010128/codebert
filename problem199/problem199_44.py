S = input()
hi = []

for i in range(5):
    hi.append("hi"*(i+1))

print("Yes" if S in hi else "No")