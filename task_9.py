import string

def count_words() -> list:
    '''
    The function count word frequencies from user input until empty string is entered.
    Words are converted to lowercase and punctuation is stripped.
    
    Returns:
        list: Sorted list of words by frequency in descending order
    '''
    words_dict = {}

    word = input().lower().strip(string.punctuation)
    while word != '':
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1

        word = input().lower().strip(string.punctuation)

    words_dict_sorted = sorted(words_dict.items(),
                               key= lambda i: i[1],
                               reverse= True)
    
    return [word[0] for word in words_dict_sorted]


def main():
    sorted_words = count_words()
    for word in sorted_words:
        print(word)


if __name__ == '__main__':
    main()