def main():
    T = input()
    ans = ""
    for i in range(len(T)):
        t = T[i]
        if t=='P' or t=='D':
            ans += t
        else:
            ans += 'D'
    print(ans)
main()
