s = input()
n = int(input())

s_array = []
for i in range(len(s)):
    s_array.append(s[i])

for i in range(n):
    order = input().split()
    if order[0] == "replace":
        first = int(order[1])
        last = int(order[2])
        for j in range(last-first+1):
            s_array[first+j] = order[3][j]
    elif order[0] == "reverse":
        a = int(order[1])
        b = int(order[2])
        buf = []
        for j in range(b, a-1, -1):
            buf.append(s_array[j])
        for j in range(b+1-a):
            s_array[a+j] = buf[j]
    elif order[0] == "print":
        a = int(order[1])
        b = int(order[2])
        for j in range(a, b+1):
            print("%s" % s_array[j], end="")
        print()
    

