n = input()
a = map(int, raw_input().split())
s = ""
for i in range(-1, -n, -1):
    s += str(a[i]) + " "
s += str(a[-n])
print(s)