
ans = []

while (1) :
    word = input().strip()
    try :
        inputLen = int( input().strip() )
    except :
        break 

    for i in range(0, inputLen) :
        h = int( input().strip() )
        word = word[h:] + word[:h]

    ans.append(word)

for s in ans :
    print(s)

