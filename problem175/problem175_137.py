from collections import Counter


def main():
    n = int(input())
    s = input()
    cnt = Counter(s)
    ans = cnt["R"] * cnt["G"] * cnt["B"]
    for gap in range(1, (n - 1) // 2 + 1):
        for i in range(n - gap * 2):
            if set([s[i], s[i + gap], s[i + 2 * gap]]) == {"R", "G", "B"}:
                ans -= 1
    print(ans)


if __name__ == "__main__":
    main()
