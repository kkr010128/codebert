sent=""
while True:
    try:
        ex=input().lower()
        sent+=ex
    except:
        break
for i in range(ord("a"),ord("z")+1):
    x=sent.count(chr(i))
    print(chr(i),":",x)