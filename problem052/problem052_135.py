def main():
    n = int(input())
    ans = []
    i = 1
    while 1:
        if i <= n:
            if i % 3 == 0:
                ans.append(i)
            else:
                hoge = list(str(i))
                if "3" in hoge:
                    ans.append(i)
            i += 1
        else:
            break
    
    print(" ", end = "")
    for x in range(len(ans)):
        if x != len(ans) - 1:
            print(ans[x], end = " ")
        else:
            print(ans[x])

if __name__ == "__main__":
    main()