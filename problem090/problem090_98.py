def main():
    s = input()
    cnt = 0
    cnt2 = 0
    for i in s:
        if i == "R":
            cnt2 += 1
        else:
            cnt = max(cnt, cnt2)
            cnt2 = 0
    print(max(cnt, cnt2))


main()
