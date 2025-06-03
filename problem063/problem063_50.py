import sys

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cnt = 26 * [0]
Input = ""
loop = True

#while loop:
#    I = input()
#    if not I:
#        loop = False
#    Input += I

for I in sys.stdin:
    Input += I

for i1 in range(len(alphabet)):
    for i2 in range(len(Input)):
        if 'A' <= Input[i2] <= 'Z':
            w = Input[i2].lower()
        else:
            w = Input[i2]
        if alphabet[i1] == w:
            cnt[i1] += 1
    print(alphabet[i1] + " : " + str(cnt[i1]))