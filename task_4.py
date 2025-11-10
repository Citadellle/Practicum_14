import re

user_list = re.split(r'[.,:;!?\-"\'() ]+', input())

new_list = list(set(user_list))

print(new_list)