while True:
    h, w = map(int, input().split(" "))
    if h == 0 and w == 0:
        break
    print("#"*w)
    print(("#"+ "."*(w-2) +"#" + "\n")*(h-2) + "#" * w) if h >2 and w>=2 else 0
    print("#"*w) if h == 2 else 0
    print("")