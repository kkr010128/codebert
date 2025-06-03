s = input()
count = 1; memo = 0; x = 0
for i in range(1, len(s)):
    if s[i-1] == "<" and s[i] == ">":
        x += count*(count-1)//2
        memo = count
        count = 1
    elif s[i-1] == ">" and s[i] == "<":
        x += count*(count-1)//2+max(count, memo)
        memo = 0
        count = 1
    else:
        count += 1
else:
    if s[-1] == "<":
        x += count*(count+1)//2
    else:
        x += count*(count-1)//2+max(count, memo)
print(x)