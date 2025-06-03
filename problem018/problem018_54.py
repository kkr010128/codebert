
def main():
    l = input().split(' ')

    while len(l) > 1:
        idx = 0
        while l[idx] not in ["+", "-", "*"]:
            idx += 1
        res = str(eval(str(l[idx-2] + l[idx] + l[idx-1])))
        l[idx-2] = res
        l.pop(idx-1)
        l.pop(idx-1)

    print(l[0])

main()
