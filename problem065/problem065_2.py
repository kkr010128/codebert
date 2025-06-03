import re
W = input()
T = []
count = 0
while(1):
    line = input()
    if (line == "END_OF_TEXT"):
        break
    words = list(line.split())
    for word in words:
        T.append(word)
    
for word in T:
    matchOB = re.fullmatch(W, word.lower())
    if matchOB:
        count += 1

print(count)