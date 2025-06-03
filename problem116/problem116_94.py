s = input()
t = input()

counter = 0
for index, character in enumerate(s):
    if t[index] != character:
        counter += 1
print(counter)