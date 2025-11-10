user_list = [int(i) for i in input('Введите элементы списка: ').split(' ')]
command = input('Введите команду: ')

orient_shift = command[0].lower()
index_shift = int(command[1])

if orient_shift == 'r':
    new_list = user_list[-index_shift:] + \
        user_list[:-index_shift]

    print(new_list)

else:
    new_list = user_list[index_shift:] + \
        user_list[:index_shift]
    
    print(new_list)