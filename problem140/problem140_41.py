import sys
input = sys.stdin.readline

t = input()

t_update = ""
for i in t:
    if i == "?":
        i = "D"
    t_update += i
print(t_update)