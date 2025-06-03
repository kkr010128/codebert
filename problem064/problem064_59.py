def search(pat, s):
    """find a pattern 'pat' in a ring shaped text 's'
    len(s) >= len(p) and both s and p consists of lowercase characters.

    >>> search('a', 'a')
    True
    >>> search('advance', 'vanceknowledgetoad')
    True
    >>> search('advanced', 'vanceknowledgetoad')
    False
    """
    return pat in s + s


def run():
    s1 = input()
    s2 = input()

    if search(s2, s1):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    run()

