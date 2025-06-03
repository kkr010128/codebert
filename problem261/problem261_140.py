
def main1():
    s = input()
    s1 = s[0:len(s)//2]
    s2 = s[::-1]
    s2 = s2[0:len(s)//2]
    ans = 0

    for i  in range(len(s)//2):
        if s1[i]==s2[i]:
            continue
        else:
            ans+=1
    print(ans)



if __name__ == '__main__':
    main1()
