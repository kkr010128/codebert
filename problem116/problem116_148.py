def Qb():
    s, t = open(0).read().splitlines()
    r = sum([s != t for s, t in zip(s, t)])
    print(r)



if __name__ == '__main__':
    Qb()
