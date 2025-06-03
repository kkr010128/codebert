#16D8101014F Kurume Ryunosuke 久留米竜之介 2018/5/16 Python3
n = int(input())
box = set()

for _ in range(n):
    tmp,mozi= input().split()
    
    if tmp == "find":
        if mozi in box:
            print("yes")
        else:
            print("no")
    else:
        box.add(mozi)
