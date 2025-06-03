S = input()

while 1:
    bef = S
    bef = bef.replace("?", "D")
    if S==bef:
        break
    S = bef
    
print(S)