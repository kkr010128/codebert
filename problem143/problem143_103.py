import sys
#長さK
K = int(input())

#文字列S
S = input()

#print(type(len(S)))
#print(type(K))
#print(str(S))

if len(S) <= K:
    print(S)
    sys.exit()

else:
    S = str(S)
    print(S[:K]+"...")
    sys.exit()
