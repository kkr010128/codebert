# coding: utf-8
from operator import add, sub, mul

op_dict = {'+': add, '-': sub, '*': mul}

def calcurate(list_):
    s = []
    for l in list_:
        if l.isdigit():
            s.append(int(l))
        elif l in ['+', '-', '*']:
            a = s.pop()
            b = s.pop()
            s.append(op_dict[l](b, a))
    return s[0]



def main():
    inputs = raw_input().split()
    print calcurate(inputs)


if __name__ == '__main__':
    main()