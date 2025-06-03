def main():
    n = int(input())
    s = input()
    one_set = set([])
    two_set = set([])
    three_set = set([])

    count = 0
    for i in range(n):
        if i==0:
            one_set.add(s[0])
            continue

        if 2<=i:
            for two in two_set:
                if two + s[i] not in three_set:
                    three_set.add(two + s[i])
                    count+=1

        for one in one_set:
            two_set.add(one + s[i])
        one_set.add(s[i])

    print(count)

if __name__=="__main__":
    main()
