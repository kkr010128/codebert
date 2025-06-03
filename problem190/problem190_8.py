s=input()

mozisuu=len(s)

def hanteiki(s):
    hantei=True
    mozisuu=len(s)
    for i in range(len(s)):
        if s[i]!=s[mozisuu-i-1]:
            hantei=False
    return hantei
            
if hanteiki(s):
    if hanteiki(s[0:(mozisuu-1)//2]):
        if hanteiki(s[(mozisuu+3)//2-1:]):
            print("Yes")
            exit()

print("No")