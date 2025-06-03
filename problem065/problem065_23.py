w = raw_input().lower()
s = 0

while 1:

    in_str = raw_input()
    if in_str == "END_OF_TEXT":
        break

    in_str = map(str, in_str.split())

    for i in in_str:
        if i.lower() == w:
            s+=1

print s