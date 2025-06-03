def main():
    n = int(input())
    nums = input().split(' ')
    s = set()
    result = 'YES'

    for i in range(n):
        num = nums[i]
        if num in s:
            result = 'NO'
            break
        s.add(num)

    print(result)


if __name__ == '__main__':
    main()
