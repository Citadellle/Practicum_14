num_3_in_list = False

while num_3_in_list == False:
    user_list = [int(i) for i in input().split(' ')]

    if user_list.count(3) != 1:
        print('Неверный ввод, введи строку,' \
              'которая содержит только одно число 3')
        continue

    num_3_in_list = True

user_list.remove(3)

print(user_list)