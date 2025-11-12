def calculate_average(user_list: list) -> float:
    '''
    Calculate the average value of a list of numbers.
    
    Args:
        numbers (list): List of numbers to calculate average for
    
    Returns:
        float: The average value of the numbers
    '''
    average_val = sum(user_list) / len(user_list)
  
    return average_val


def main():
    user_list = [int(i) for i in input().split(' ')]
    average = calculate_average(user_list)
    print(average)


if __name__ == '__main__':
    main()
