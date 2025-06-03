def main():
    n = int(input())
    bit = input()[::-1]
    count = bit.count("1")
    count_plus = count+1
    count_minus = count-1
    pow_plus = [1 % count_plus]
    for i in range(n):
        pow_plus.append(pow_plus[-1]*2 % count_plus)
    if count_minus != 0:
        pow_minus = [1 % count_minus]
        for i in range(n):
            pow_minus.append(pow_minus[-1]*2 % count_minus)
    else:
        pow_minus = []

    bit_plus = 0
    bit_minus = 0

    for i in range(n):
        if bit[i] == "1":
            bit_plus = (bit_plus+pow_plus[i]) % count_plus
    if count_minus != 0:
        for i in range(n):
            if bit[i] == "1":
                bit_minus = (bit_minus+pow_minus[i]) % count_minus
    ans = []
    for i in range(n):
        if bit[i] == "1":
            if count_minus == 0:
                ans.append(0)
                continue
            bit_ans = (bit_minus-pow_minus[i]) % count_minus
            count = count_minus
        else:
            bit_ans = (bit_plus+pow_plus[i]) % count_plus
            count = count_plus
        cnt = 1
        while bit_ans:
            b = str(bin(bit_ans)).count("1")
            bit_ans = bit_ans % b
            cnt += 1
        ans.append(cnt)
    for i in ans[::-1]:
        print(i)


main()
