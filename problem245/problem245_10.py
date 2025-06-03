n = int(input())
s = input()
s = list(s)

count = 0
while len(s) > 2:
    if s[0] == "A" and s[1] =="B" and s[2] == "C":
        count += 1
        del s[0:2]
    else:
        del s[0]

print(count)
