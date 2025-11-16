def number_of_hole_lets(word: str) -> int:
    '''
    The function takes a string as an argument and
    outputs the number of letters with holes.

    Args:
        str: Input text to analyze
        
    Returns:
        int: Number of letters with holes
    '''
    lets_list = [i for i in word 
                 if i in 'a,b,d,e,g,o,p,q']
    return len(lets_list)


def number_of_not_hole_lets(word: str) -> int:
    '''
    The function takes a string as an argument and
    outputs the number of letters without holes.

    Args:
        str: Input text to analyze
        
    Returns:
        int: Number of letters without holes
    '''
    lets_list = [i for i in word 
                 if i not in 'a,b,d,e,g,o,p,q']
    return len(lets_list)


def get_words_with_2_or_more_holes(words: list) -> list:
    '''
    The function creates a list of words with two or more letters with holes.
    
    Args:
        list: User list of words
        
    Returns:
        list: List of words with two or more letters with holes
    '''
    words_with_2_or_mr_hole_lets = []
    for word in words:
        if number_of_hole_lets(word) >= 2:
            words_with_2_or_mr_hole_lets.append(word)  
    
    return words_with_2_or_mr_hole_lets


def main() -> None:
    '''
    Main function that performs string analysis for letters with holes.

    Function:
    1. Requests a string from the user
    2. Breaks the string into words
    3. Counts the number of letters with and without holes
    4. Makes a list of words with 2 or more letters with holes.
    5. Displays the number of letters with and without holes, and 
    a list of words with 2 or more letters with holes.
    '''
    string = input('Введите строку: ')
    words = string.split(' ')

    print(f'Количество букв с отверстиями: {number_of_hole_lets(string)}',
          f'Количество букв без отверстий: {number_of_not_hole_lets(string)}',
          f'Список слов, имеющих две и более букв \
            с отверстиями: {get_words_with_2_or_more_holes(words)}',
          sep= '\n')


if __name__ == '__main__':
    main()