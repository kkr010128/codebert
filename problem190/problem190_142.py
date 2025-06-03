word = input()
n = len(word)
hanbun = int((n-1)/2)
notk = 0
for i in range(hanbun):
    if word[i] != word[n-i-1]:
        notk = 1
        break
        
if hanbun % 2 == 0:
    hanbun2 = int(hanbun/2)
else:
    hanbun2 = int((hanbun-1)/2)
    
for j in range(hanbun2):
    if word[j] != word[hanbun-j-1]:
        notk = 1
        break

if notk == 1:
    print('No')
else:
    print('Yes')