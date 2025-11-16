def string_sort(user_string: str) -> str:
    '''
    The function accepts a string as input, converts the string to a list of characters,
    sorts the list, converts the list back to a string, and returns the final string.

    Args:
        str: Input string to be sorted
        
    Returns:
        str: New string with sorted symbols in alphabetical order
    '''
    string_as_list = [i for i in user_string]
    string_as_list.sort()

    new_string = ''.join(string_as_list)

    return new_string


def main() -> None:
    '''
    The main function is to get the user's string, convert the string 
    into a sorted string, and output the resulting string.

    Functions used:
    - string_sort(): converting a string argument to a list, sorting the list, 
    converting the list back to a string, and returning the final string.
    '''
    user_string = input('Введите строку: ')

    final_list = string_sort(user_string)

    print(final_list)


if __name__  == '__main__':
    main()