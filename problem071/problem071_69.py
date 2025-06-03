def solve():
    string = list(input())
    ans = 0
    if string[-1]=="s":
        ans = "".join(string)+"es"
        print(ans)
        return 
    else:
        print("".join(string)+"s")
        return

solve()