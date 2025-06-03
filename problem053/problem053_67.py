n = int(raw_input())
a = []
input_line = raw_input().split()
for i in input_line:
    a.append(i)
for i in reversed(a):
    print i,