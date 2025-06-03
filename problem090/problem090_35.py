#A問題

S = input()
if S == "RRR":
    print(3)
if S == "RRS"or S == "SRR" :
    print(2)
if S == "RSR"or S == "RSS" or S == "SRS" or S == "SSR":
    print(1)
if S == "SSS":
    print(0) 