s = input()
p = input()
p_len = len(p)

if p in s:
    print("Yes")
else:
    for i in range(p_len):
        if (p[:i] == s[-i:]) and (p[i:] == s[:p_len - i]):
            print("Yes")
            break
    else:
        print("No")