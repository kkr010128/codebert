count_al = list(0 for i in range(26))
while True :
    try :
        a = str(input())
        b = a.lower()
        for i in range(len(b)) :
            c = ord(b[i])
            if c > 96 and c < 123 :
                count_al[c - 97] += 1
    except EOFError :
        break
    
for i in range(97, 123) :
    print(chr(i), ":", count_al[i-97])
