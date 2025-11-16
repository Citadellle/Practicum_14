def get_user_input() -> tuple:
    '''
    The function get user input as two lists and range indices.
    
    Returns:
        tuple:
            list_1 (list): First list of integers
            list_2 (list): Second list of integers
            range_start (int): Start index of the range
            range_end (int): End index of the range
    '''
    list_1 = [int(i) for i in input('Введите элементы 1-го списка: ').split(' ')]
    list_2 = [int(i) for i in input('Введите элементы 2-го списка: ').split(' ')]
    range_start = int(input('Введите начало среза: ')) - 1
    range_end = int(input('Введите конец среза: '))
    
    return list_1, list_2, range_start, range_end


def transfer_elements(list_1: list, list_2: list, range_start: int, range_end: int) -> tuple:
    '''
    The function transfers elements from range_start to range_end (inclusive) from list_1 to list_2
    in reverse order, then removes these elements from list_1.
    
    Args:
        list_1 (list): Source list to transfer elements from
        list_2 (list): Target list to add elements to
        range_start (int): Start index of the range
        range_end (int): End index of the range
        
    Returns:
        tuple: Modified list_1 and list_2 after transfer operation
    '''
    # Extract elements in reverse order and extend list_2
    list_2.extend(list_1[range_end : range_start - 1 : -1])
    
    # Remove transferred elements from list_1
    del list_1[range_start : range_end + 1]
    
    return list_1, list_2


def main():
    list_1, list_2, range_start, range_end = get_user_input()
    
    list_1_final, list_2_final = transfer_elements(list_1, list_2, range_start, range_end)

    print(f'Список 1: {list_1_final}',
          f'Список 2: {list_2_final}',
          sep= '\n')


if __name__ == '__main__':
    main()