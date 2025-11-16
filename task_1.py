def get_user_list() -> list:
    '''
    The function get a list of 10 integers numbers from user input.
    
    Returns:
        list: List of 10 numbers entered by the user
    '''
    user_list = [int(input()) for i in range(10)]
    
    return user_list


def calculate_sums(user_list: list) -> list:
    '''
    The function calculate sums of adjacent elements in a list.
    
    Args:
        list: list of numbers to process
        
    Returns:
        list: new list where each element is the sum of two
        adjacent elements from the user_list
    '''
    new_list = []
    for i in range(len(user_list) - 1):
        new_list.append(user_list[i] + user_list[i+1])
        
    return new_list


def main():
    user_list = get_user_list()
    result_list = calculate_sums(user_list)
    print(result_list)


if __name__ == '__main__':
    main()