a=ord('a')
rdif=range(ord('z')-a+1)
l=[0 for _ in rdif]
s=''
while True:
    try: s+=input().lower()
    except: break    
for i in range(len(s)):
    if s[i].isalpha(): l[ord(s[i])-a]+=1
for i in rdif:
    print(chr(i+a),':',l[i])