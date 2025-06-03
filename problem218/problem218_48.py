n=int(input())
wl={}
for i in range(n):
    w=input()
    if w not in wl:
        wl[w]=0
    wl[w]+=1
wm=max(wl.values())
wl3=sorted(wl.items())
for i in range(len(wl3)):
    if wl3[i][1]==wm:
        print(wl3[i][0])