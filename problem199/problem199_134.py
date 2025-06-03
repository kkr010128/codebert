S = list(input())

word_num = int(len(S)/2)

temp_num = 0

if len(S) % 2 == 0:
    for i in range(word_num):
        if S[2*i]+S[2*i+1] == 'hi':
            pass
        else:
            temp_num += 1
else:
    pass

if len(S) % 2 == 0 and temp_num == 0:
    print('Yes')
else:
    print('No')