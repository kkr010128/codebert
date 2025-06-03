"""test programm for Q-B 20200719 """
# test programm for B


def __main__():
    str1 = str(input())
    str2 = str(input())
    list_str1 = list(str1)
    list_str2 = list(str2)

    if len(list_str1) < 1 or 2*10**5 < len(list_str1):
        raise ValueError
    elif str1.isalpha() == False or str1.islower() == False:
        raise ValueError
    elif str2.isalpha() == False or str2.islower() == False:
        raise ValueError
    elif len(str1) != len(str2):
        raise ValueError

    cnt = 0
    for n in range(len(list_str1)):
        if list_str1[n] != list_str2[n]:
            cnt += 1
        else:
            continue

    print(cnt)


if __name__ == "__main__":
    __main__()