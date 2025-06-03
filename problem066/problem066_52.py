s = ""
while True:
    s = input()
    if s == "-": break
    loop_cnt = int(input())
    for i in range(loop_cnt):
        h = int(input())
        s = s[h:] + s[:h]
    else:
        print(s)