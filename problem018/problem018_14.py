import operator
def poland(A):
    l = []
    ops = { "+": operator.add, "-": operator.sub, '*' : operator.mul }
    for i in range(len(A)):
        item = A.pop(0)
        if item in ops:
            l.append(ops[item](l.pop(-2),l.pop()))
        else:
            l.append(int(item))
    return l.pop()
    

if __name__ == '__main__':
    A = input().split()
    print (poland(A[:]))