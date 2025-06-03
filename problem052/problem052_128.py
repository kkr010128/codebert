k = int(input())


def call(m: int) -> str:
    result = ""
    for i in range(1, m + 1):
        if i % 3 == 0 or '3' in str(i): 
            result += " " + str(i)
    return result


print(call(k))

