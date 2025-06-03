word=input().lower()
how_in=0
while True:
    letters=input()
    if letters=='END_OF_TEXT':
        break
    for i in letters.lower().split():
        if i==word:
            how_in+=1
print(how_in)