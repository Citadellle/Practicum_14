nums_list = [int(i) for i in input().split(' ')]

even_nums_sum = sum([i for i in nums_list if i % 2 == 0])
odd_nums_sum = sum([i for i in nums_list if i % 2 != 0])

print(f'Сумма четных элементов: {even_nums_sum}',
      f'Сумма нечетных элементов: {odd_nums_sum}',
      sep= '\n')