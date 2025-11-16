import re
import string


def split_and_get_unique_words(text: str) -> list:
    '''
    The function split text into words, removing all punctuation and return unique words.
    
    Args:
        str: Input text to process
    
    Returns:
        list: List of unique words without punctuation
    '''
    pattern = re.escape(string.punctuation)
    user_list = re.split(f'[{pattern} ]+', text)
    new_list = list(set(user_list))
  
    return new_list


def main():
    text = input()
    unique_words = split_and_get_unique_words(text)
    print(unique_words)


if __name__ == '__main__':
    main()