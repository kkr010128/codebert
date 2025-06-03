def abc173d_chat_in_the_circle():
    n = int(input())
    a = sorted(map(int, input().split()), reverse=True)
    if n <= 1:
        print(0)
        return
    val = 0
    for i in range(0, n-1):
        idx = (i+1) // 2
        val += a[idx]
    print(val)

abc173d_chat_in_the_circle()