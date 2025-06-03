W=input()

T=""
while True:
    line_sentence=input()
    if line_sentence=="END_OF_TEXT":
        break
    T+=" "+line_sentence.lower()

t=T.split()

cnt=0
for w in t:
    if w==W:
        cnt+=1

print(cnt)