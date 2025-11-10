user_list = [int(input()) for i in range(10)]

new_list = []
for i in range(len(user_list) - 1):
    new_list.append(user_list[i] + user_list[i+1])

print(new_list)