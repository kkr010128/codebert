score = list(map(int,input().split()))
if score[0] == 1:
    evennum = 0
else:
    evennum = score[0]*(score[0]-1)/2
if score[1] == 1:
    oddnum = 0
else:
    oddnum = score[1]*(score[1]-1)/2
print(int(evennum+oddnum))