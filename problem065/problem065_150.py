w = input()
t = ""
while 1:
    try:
        t += input().lower()
        t += " "
    except EOFError:
        break
s = t.split()
count = 0
for i in s:
    if i == w:
        count += 1
print(count)