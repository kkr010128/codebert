n = int(input())
s = input()

cnt = 0

for i in range(len(s)):
    if s[i] == "A" and i+2 <= len(s)-1:
        if s[i+1] == "B":
            if s[i+2] == "C":
                cnt += 1 
print(cnt)