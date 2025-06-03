English_sentence=''
try:
    while True:
        line=input()
        if line=='':
            break
        English_sentence+=line
except EOFError:
	pass
lowercase=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for _ in range(26):
    for _2 in English_sentence:
        if _2==lowercase[_] or _2==uppercase[_]:
            number[_]+=1
for ans in range(26):
    print("{0} : {1}".format(lowercase[ans],number[ans]))
