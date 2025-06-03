str = input()
q = int(input())
for x in range(q):
    en = input().split()
    if en[0] == "print":
        print(str[int(en[1]):int(en[2])+1])
    elif en[0] == "reverse":
        str = str[:int(en[1])] + str[int(en[1]):int(en[2])+1][::-1] + str[int(en[2])+1:]
    else:
        str = str[:int(en[1])] + en[3] + str[int(en[2])+1:]


