import re
import string

pattern = re.escape(string.punctuation)
user_list = re.split(f'[{pattern} ]+', input())

new_list = list(set(user_list))

print(new_list)
