S = input()
count = 0
if S[2] == S[3]:
    count+=1
if S[4] == S[5]:
    count+=1
if count == 2:
    print('Yes')
else:
    print('No')