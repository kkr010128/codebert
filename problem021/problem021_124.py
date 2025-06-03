def main():
    s = input()
    lst1 = []
    lst2 = []
    total_area = 0

    for i in range(len(s)):
        if s[i] == "\\":
            lst1.append(i)
        elif s[i] == "/" and len(lst1) > 0:
            j = lst1.pop()
            area = i - j
            total_area += area
            while len(lst2) > 0 and lst2[-1][0] > j:
                area += lst2.pop()[1]
            lst2.append([j, area])
    print(total_area)
    print(len(lst2), *[area for j, area in lst2])


if __name__ == "__main__":
    main()

