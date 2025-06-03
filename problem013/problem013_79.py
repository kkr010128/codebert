# coding: utf-8

def getint():
    return int(input().rstrip())

def main():
    n = getint()

    values = []
    for i in range(n):
        values.append(getint())

    maxv = values[1] - values[0]
    minv = values[0]
    for j in range(1,n):
        maxv = max(maxv, values[j]-minv)
        minv = min(minv, values[j])

    print(maxv)
    
if __name__ == '__main__':
    main()