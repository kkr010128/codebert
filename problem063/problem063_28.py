wordcount = ""
while True:
    try:
        words = input()
        wordcount = wordcount + words.lower()
    except:
        break    
for i in [chr(i) for i in range(97,97+26)]:
    print('{0} : {1}'.format(i,wordcount.count(i)))