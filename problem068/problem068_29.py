s = input()
for _ in range(int(input())):
    code=input().split()
    if code[0]=='print'  :
        print("".join(s[int(code[1]):int(code[2])+1]))
    elif code[0]=='reverse':
        s = s[:int(code[1])] + s[int(code[1]):int(code[2])+1][::-1] + s[int(code[2])+1:]
    elif code[0]=='replace':
        s = s[:int(code[1])] + code[3] + s[int(code[2])+1:]