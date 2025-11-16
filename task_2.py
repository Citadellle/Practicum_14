def remove_number_3() -> list:
    '''
    Requests user for input until a list with exactly one '3'.
    Then removes the number 3 from the list and returns the modified list.

    Returns:
        list: The original user list with the number 3 removed
    '''
    num_3_in_list = False

    while num_3_in_list == False:
        user_list = [int(i) for i in input().split(' ')]

        if user_list.count(3) != 1:
            print('Неверный ввод, введи строку, которая содержит только одно число 3')
            continue

        num_3_in_list = True

    user_list.remove(3)

    return user_list


def main():
    result_list = remove_number_3()
    print(result_list)


if __name__ == '__main__':
    main()