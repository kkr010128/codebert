n = 0
T=""
s= input().lower()
while True:
    t=input()
    T += t + " "
    if T.count("END_OF_TEXT")>0:
        break

TL = T.split(" ")

for i in TL:
    i = i.replace('"','')
    i= i.replace(".","")
    if i.lower() == str(s):
        n += 1
    else:
        pass
print (n)