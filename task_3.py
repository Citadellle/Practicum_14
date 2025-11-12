import re
import string

pattern = re.escape(string.punctuation)
list_words = re.split(f'[{pattern} ]+', input())

print(list_words)
