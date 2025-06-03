def a():
    a = "1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51"
    list_a = a.split(sep=",")
    k = int(input())
    print(list_a[k-1])
    

if __name__ == '__main__':
    a()