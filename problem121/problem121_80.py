n = int(input())

digits = []
letters = ''

while n > 0:
    digits.append((n-1) % 26)
    n = (n -1) // 26

for x in digits[::-1]:
    letters += chr(x+97)
print(letters)
