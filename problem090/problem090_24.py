def check_weather(weathers: str) -> int:
    count = 0
    l_n = [0]
    for index, i in enumerate(weathers):
        if weathers[-1] == 'R' and index == len(weathers) - 1:
            count += 1
            l_n.append(count)
            break

        if i == 'R':
            count += 1
        else:
            if max(l_n) <= count:
                l_n.append(count)
            count = 0
    return max(l_n)


if __name__ == '__main__':
    print(check_weather(input()))