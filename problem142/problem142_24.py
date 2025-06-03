num = list(map(int,input()))
if num[-1] == 3:
    print("bon")
    
elif num[-1] in (0, 1, 6, 8):
    print("pon")
    
else:
    print("hon")
