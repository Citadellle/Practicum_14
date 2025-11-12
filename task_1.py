def calculate_sums(user_list: list) -> list:
    '''
    Calculate sums of adjacent elements in a list.
    
    Args:
        list: list of numbers to process
        
    Returns:
        list: new list where each element is the sum of two adjacent elements
              from the user_list
    '''
    new_list = []
    for i in range(len(user_list) - 1):
        new_list.append(user_list[i] + user_list[i+1])
    return new_list


def main():
    user_list = [int(input()) for i in range(10)]
    
    result_list = calculate_sums(user_list)

    print(result_list)


if __name__ == '__main__':
    main()

