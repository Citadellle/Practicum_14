import re
import string


def split_text_into_words(text: str) -> list:
    '''
    The function split text into words, removing all punctuation.
    
    Args:
        str: Input text to split
    
    Returns:
        list: List of words without punctuation
    '''
    pattern = re.escape(string.punctuation)
    list_words = re.split(f'[{pattern} ]+', text)
    
    return list_words


def main():
    text = input()
    words = split_text_into_words(text)
    print(words)


if __name__ == '__main__':
    main()