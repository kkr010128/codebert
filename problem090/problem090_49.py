if __name__ == "__main__":
    S = input()
    list_s = [s for s in S]
    ans = 0
    if list_s[0] == 'S' and list_s[1] == 'S' and list_s[2] == 'S':
        ans = 0
    elif list_s[0] == 'S' and list_s[1] == 'S' and list_s[2] == 'R':
        ans = 1
    elif list_s[0] == 'S' and list_s[1] == 'R' and list_s[2] == 'R':
        ans = 2
    elif list_s[0] == 'R' and list_s[1] == 'R' and list_s[2] == 'R':
        ans = 3
    elif list_s[0] == 'R' and list_s[1] == 'S' and list_s[2] == 'R':
        ans = 1
    elif list_s[0] == 'R' and list_s[1] == 'R' and list_s[2] == 'S':
        ans = 2
    elif list_s[0] == 'R' and list_s[1] == 'S' and list_s[2] == 'S':
        ans = 1
    elif list_s[0] == 'S' and list_s[1] == 'R' and list_s[2] == 'S':
        ans = 1

    print(ans)




