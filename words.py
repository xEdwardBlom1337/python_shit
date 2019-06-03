def load_words():
    with open('words.txt') as word_file:
        valid_words = word_file.read().split()

    return valid_words

def contains_chars(string, chars):
    for char in string:
        if char not in chars:
            return False
    return True

if __name__ == '__main__':
    words = load_words()
    longest_words = []
    for word in words:
        if contains_chars(word, 'abcdefhjlnprstuy'):
            longest_words.append(word)
    # print(longest_words)

    longest = longest_words[0]
    for word in longest_words:
        if len(word) >= len(longest):
            longest = word
    print(longest)
