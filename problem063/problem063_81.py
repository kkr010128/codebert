alphabets = "abcdefghijklmnopqrstuvwxyz"
#print(len(alphabets))
#a = len(alphabets)
#print(a)
x = ''
while True:
    try:
        x += input().lower()
    except EOFError:
        break

for i in range(len(alphabets)):
    print("{0} : {1}".format(alphabets[i], int(x.count(alphabets[i]))))