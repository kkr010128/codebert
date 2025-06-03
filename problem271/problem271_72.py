n = int(input())
s = input()
out = ""
for i in s:
    if ord(i) + n > 90:
        out += chr(64+n-(90-ord(i)))
    else:    
        out += chr(ord(i)+n)

print(out)