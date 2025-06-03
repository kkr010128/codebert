chars = [chr(i) for i in range(ord('a'), ord('z') + 1)]

arr = []

x = int(input())


def get_len(n):
    length = 1
    t = 26

    while True:
        if n <= t:
            return length
        t += 26 ** (length + 1)
        length += 1

        if length > 1000000000000001:
            raise


def get_ord(n):
    st = 1
    end = 26
    ind = 1
    while True:
        if st <= n <= end:
            return x - st

        st = end + 1
        end += 26 ** (ind + 1)
        ind += 1


length = get_len(x)
order = get_ord(x)
# print(length)

for i in range(length):
    s = order % 26
    order = order // 26
    arr.append(s)

# print(arr)

ans = ""
for ai in arr[::-1]:
    ans += chars[ai]
print(ans)