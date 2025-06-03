count={}
for i in range(97,97+26):
    count[chr(i)] = 0

text=[]
while True:
    try:
        text.append(input())
    except EOFError:
        break

text_out="".join(text)
text_lower=text_out.lower()

for letter in text_lower:
    if letter in count:
        count[letter] += 1

for x,y in sorted(count.items()):
    print("{0} : {1}".format(x,y))