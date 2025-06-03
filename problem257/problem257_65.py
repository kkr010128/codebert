# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline

    n = int(input().rstrip())

    count = 0
    ans = 0
    for a in input().rstrip().split(" "):
        a = int(a)
        if a == count + 1:
            count+= 1
        else:
            ans += 1

    if count == 0:
        print("-1")
    else:
        print(ans)

if __name__ == "__main__":
    resolve()
