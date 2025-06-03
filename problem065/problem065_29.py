def main():

    target_word = str(input()).lower()
    texts_tuple = tuple()
    
    while True:
        text = input()
        if text == 'END_OF_TEXT': break
        texts_tuple += tuple(text.lower().split())
    
    print(texts_tuple.count(target_word))


main()