n = int(input())
c0 = 0
c1 = 0
c2 = 0
c3 = 0
for i in range(n):
    s = input()
    if s == "AC":
        c0 += 1
    elif s == "WA":
        c1 += 1
    elif s == "TLE":
        c2 += 1
    elif s == "RE":
        c3 += 1
    else:
        exit()

print(f"AC x {c0}")
print(f"WA x {c1}")
print(f"TLE x {c2}")
print(f"RE x {c3}")
