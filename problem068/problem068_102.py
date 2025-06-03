bun=input()
for i in range(int(input())):
    o=input().split()
    o[1],o[2]=int(o[1]),int(o[2])
    if o[0]=='print':
        print(bun[o[1]:o[2]+1])
    elif o[0]=='reverse':
        bun_bun=bun[o[1]:o[2]+1]
        bun_bun=bun_bun[::-1]
        bun=bun.replace(bun[o[1]:o[2]+1],bun_bun)
    elif o[0]=='replace':
        bun=bun[:(o[1])]+o[3]+bun[(o[2]+1):]
