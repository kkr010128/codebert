import sys
read = sys.stdin.buffer.read
s = read().decode("utf-8")
H = s[:(len(s) - 1) // 2]
B = s[(len(s) - 1) // 2 + 1:-1]

if s[:-1] == s[:-1][::-1] and H == H[::-1] and B == B[::-1]:
    print("Yes")
else:
    print("No")