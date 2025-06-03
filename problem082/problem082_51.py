def count(s1, s2):
    dst = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2: dst+=1

    return dst

def execute(S, T):
    dst = len(T)

    for i in range(len(S) - len(T)+1):
        s = S[i:i+len(T)]
        c = count(s, T)
        if c < dst:
            dst = c

    return dst

if __name__ == '__main__':
    S = input()
    T = input()

    print(execute(S, T))