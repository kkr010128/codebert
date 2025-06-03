s = input()
while "?" not in s:
    s.replace("/","//")
    print(int(eval(s)))
    s = input()