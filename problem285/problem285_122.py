a = [0]
n = 0

def main():
    global n
    for s in input():
        if s == "<":
            nproc()
            a.append(a[-1]+1)
        else:
            n += 1
    nproc()
    print(sum(a))

def nproc():
    global n, a
    if n > 0 and n > a[-1]:
        a[-1] = n
    for i in list(range(n))[::-1]:
        a.append(i)
    n = 0

if __name__ == "__main__":
    main()