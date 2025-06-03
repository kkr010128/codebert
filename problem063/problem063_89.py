count = [0 for i in range(26)]
while(1):
    try:
        str = raw_input().lower()
    except EOFError:
            break
    
    for i in range(len(str)):
        k = 97
        for j in range(26):
            if str[i] == chr(k):
                count[j] += 1
            k += 1

k = 97
for i in range(26):
    print "%s : %d" % (chr(k), count[i])
    k += 1