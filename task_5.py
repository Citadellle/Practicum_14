def get_user_list() -> list:
    '''
    The function generates a list of integers entered in one line separated by a space.
    
    Returns:
        list: List of numbers entered by the user
    '''
    user_list = [int(i) for i in input().split(' ')]

    return user_list


def calculate_average(user_list: list) -> float:
    '''
    The function calculates the average value for a list of numbers.
    
    Args:
        list: List of numbers to calculate average

    Returns:
        float: The average value of the numbers
    '''
    average_val = sum(user_list) / len(user_list)
  
    return average_val


def main():
    user_list = get_user_list()
    average = calculate_average(user_list)
    print(average)


if __name__ == '__main__':
    main()
