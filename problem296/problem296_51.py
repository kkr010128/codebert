def main():
    s = input()
    k = int(input())

    count_l = []
    i = 0
    counter = 1
    while True:
        if len(s) == 1:
            count_l.append(counter)
            break
        elif s[i] == s[i+1]:
            counter += 1
        else:
            count_l.append(counter)
            counter = 1
        i += 1
        if i == len(s)-1:
            if counter == 1:
                break
            else:
                count_l.append(counter)
                break

    answer = 0
    if len(count_l) >= 3 and s[0] == s[-1] and k >= 2:
        sub_l = [count_l[0] + count_l[-1]] + count_l[1:-1]
        for i in range(len(sub_l)):
            answer += (sub_l[i] // 2) * (k - 1)
        for j in range(len(count_l[:-1])):
            answer += count_l[j] // 2
        answer += count_l[-1] // 2
    elif len(count_l) == 1:
        answer += (count_l[0] * k) // 2
    else:
        for i in range(len(count_l)):
            answer += (count_l[i] // 2) * k

    print(answer)


if __name__ == "__main__":
    main()
