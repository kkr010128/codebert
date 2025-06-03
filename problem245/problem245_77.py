n = int(input())
s = input()

output = 0
for index in range((n+1)-3):
    if s[index:index+3] == "ABC":
        output += 1
print(output)