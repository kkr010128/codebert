def main():
    n = int(input())
    ans = n * (n + 1) - 1  # 1とk 自信
 
    i = 2
    while i * i <= n:
        num = n // i
        min_i = i * i
        max_i = i * num
        ans += (num - i + 1) * (min_i + max_i)  # 自分自身
        ans -= min_i
        i += 1
    print(ans)
 
 
if __name__ == "__main__":
    main()