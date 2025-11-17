def get_user_list() -> list:
    '''
    The function generates a list of integers entered in one line separated by a space.
    
    Returns:
        list: List of numbers entered by the user
    '''
    user_list = [int(i) for i in input().split(' ')]

    return user_list


def calculate_sum_even_numbers(numbers: list) -> int:
    '''
    Calculate the sum of even numbers in a list.
    
    Args:
        list: List of numbers to process
    
    Returns:
        int: The sum of even numbers
    '''
    even_nums_sum = sum([i for i in numbers if i % 2 == 0])
    
    return even_nums_sum


def calculate_sum_odd_numbers(numbers: list) -> int:
    '''
    Calculate the sum of odd numbers in a list.
    
    Args:
        list: List of numbers to process
    
    Returns:
        int: The sum of odd numbers
    '''
    odd_nums_sum = sum([i for i in numbers if i % 2 != 0])
    
    return odd_nums_sum


def main():
    numbers_list = get_user_list()
    even_sum = calculate_sum_even_numbers(numbers_list)
    odd_sum = calculate_sum_odd_numbers(numbers_list)
    
    print(f'Сумма четных элементов: {even_sum}',
          f'Сумма нечетных элементов: {odd_sum}',
          sep='\n')


if __name__ == '__main__':

    main()
