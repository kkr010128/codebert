
def main():
    x, n = map(int, input().split(" "))
    p =[]
    dif = 1e2
    ans = 0
    l_a = [i for i in range(102)]
    if n != 0:
        p = list(map(int, input().split(" ")))
    for ele in l_a[::-1]:
        if abs(x - ele) <= dif and ele not in p:
            ans = ele
            dif = abs(x - ele)
    print(ans)
if __name__ == "__main__":
    main()