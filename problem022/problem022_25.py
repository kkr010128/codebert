# ALDS1_4_A.
# リニアサーチ。

def intinput():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    return a

def main():
    n = int(input())
    S = intinput()
    q = int(input())
    T = intinput()
    count = 0
    for k in T:
        if k in S: count += 1
    print(count)

    
if __name__ == "__main__":
    main()
