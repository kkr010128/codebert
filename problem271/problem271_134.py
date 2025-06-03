N = int(input())

S = input()

def alpha2num(alpha):
    num=0
    for index, item in enumerate(list(alpha)):
        num += pow(26,len(alpha)-index-1)*(ord(item)-ord('A')+1)
    return num


def num2alpha(num):
    if num<=26:
        return chr(64+num)
    elif num%26==0:
        return num2alpha(num//26-1)+chr(90)
    else:
        return num2alpha(num//26)+chr(64+num%26)

li = []

for s in S:
    num = alpha2num(s)
    num += N
    num %= 26
    if num==0:
        num = 26
    ap = num2alpha(num)
    li.append(ap)


print("".join(li))