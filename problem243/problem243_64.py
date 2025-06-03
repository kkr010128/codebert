def main():
    musics = int(input())
    title = []
    time = []
    for _ in range(musics):
        s, t = input().split()
        title.append(s)
        time.append(int(t))
    last_song = input()
    for i in range(musics):
        if title[i] == last_song:
            print(sum(time[i + 1:]))
            break


if __name__ == '__main__':
    main()

