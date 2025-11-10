list_1 = [int(i) for i in input('Введите элементы 1-го списка: ').split(' ')]
list_2 = [int(i) for i in input('Введите элементы 2-го списка: ').split(' ')]
range_start = int(input('Введите начало среза: ')) - 1
range_end = int(input('Введите конец среза: '))

list_2.extend(list_1[range_end : range_start - 1 : -1])
del list_1[range_start : range_end + 1]

print(f'Список 1: {list_1}',
      f'Список 2: {list_2}',
      sep= '\n')