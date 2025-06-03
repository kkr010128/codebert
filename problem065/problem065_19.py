def count(word, text):
    """Count the word in text.
    Counting is done case-insensitively.

    >>> count('a', 'A b c a')
    2
    >>> count('computer', 'Nurtures computer scientists' \
              + ' and highly-skilled computer engineers' \
              + ' who will create and exploit "knowledge"' \
              + ' for the new era. Provides an outstanding' \
              + ' computer environment.')
    3
    """
    return (text
            .lower()
            .split()
            .count(word.lower()))


def run():
    word = input()
    text = ""

    line = input()
    while line != "END_OF_TEXT":
        text += line + "\n"
        line = input()

    print(count(word, text))


if __name__ == "__main__":
    run()
