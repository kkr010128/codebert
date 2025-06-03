_ = input()
a = list(input())
cnt = 0
word = 0
for i in a:
    if word == 0 and i == 'A':
        word = 1
    elif word == 1 and i =='B':
        word = 2
    elif word == 2 and i =='C':
        word = 0
        cnt += 1
    else:
        if i == 'A': 
            word = 1
        else:
            word = 0
print(cnt)