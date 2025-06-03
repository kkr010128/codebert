s = input()

flg = False
for i in range(1,6):
    if s == 'hi' *i:
        flg = True
        break
    
print('Yes' if flg else 'No')