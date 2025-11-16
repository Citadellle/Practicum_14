def get_user_input() -> tuple:
    '''
    The function get user input as the list and shift command.
    
    Returns:
        tuple:
            list: List of integers entered by user
            str: Shift command in format 'R5' or 'L3'
    '''
    user_list = [int(i) for i in input('Введите элементы списка: ').split(' ')]
    command = input('Введите команду: ')
    
    return user_list, command


def parse_command(command: str) -> tuple:
    '''
    The function parse the shift command to get orientation and value of shift.
    
    Args:
        str: Command in format 'R5' or 'L3'
        
    Returns:
        tuple:
            str: 'r' for right shift, 'l' for left shift
            int: Value of positions to shift
    '''
    orient_shift = command[0].lower()
    value_shift = int(command[1:])
    
    return orient_shift, value_shift


def shift_list(user_list: list, orient_shift: str, value_shift: int) -> list:
    '''
    The function perform cyclic shift of the list in specified orientation.
    
    Args:
        tuple:
            list: Original list to shift
            str: 'r' for right shift, 'l' for left shift
            int: Value of positions to shift
        
    Returns:
        list: New list after cyclic shift
    '''
    if orient_shift == 'r':
        # Right shift: take last 'shift_count' elements and put them at the beginning
        new_list = user_list[-value_shift:] + user_list[:-value_shift]
    else:
        # Left shift: take first 'shift_count' elements and put them at the end
        new_list = user_list[value_shift:] + user_list[:value_shift]
    
    return new_list


def main():
    user_list, command = get_user_input()
    
    orient_shift, value_shift = parse_command(command)
    
    shifted_list = shift_list(user_list, orient_shift, value_shift)
    
    print(shifted_list)


if __name__ == '__main__':
    main()