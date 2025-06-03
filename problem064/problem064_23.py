def check(s, p):
    for i in range(len(s)):
        count = 0
        for j in range(len(p)):
            if s[(i+j) % len(s)] != p[j]:
                break
            count += 1
        if count == len(p):
            return True
    return False

s = raw_input()
p = raw_input()
flag = check(s, p)
if flag:
    print("Yes")
else:
    print("No")