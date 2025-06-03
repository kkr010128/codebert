str = input()

s_ans = 'Yes'
if len(str)%2 == 1:
    s_ans ='No'
else:
    for i in range(0,len(str),2):
        moji = str[i:i+2]
        if str[i:i+2] != 'hi':
            s_ans = 'No'
            break
print(s_ans)