def fina(n, fina_list):

    if n <= 1:
        fina_list[n] = 1
        return fina_list[n]
    elif fina_list[n]:
        return fina_list[n]
    else:
        fina_list[n] = fina(n-1, fina_list) + fina(n-2, fina_list)
        return fina_list[n]


n = int(input())
fina_list = [None]*(n + 1)
print(fina(n, fina_list))

