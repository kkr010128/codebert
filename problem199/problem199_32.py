s = input()
L = s.split("hi")
ans = 1
for x in L:
    if x != "":
        ans = 0
print(["No","Yes"][ans])