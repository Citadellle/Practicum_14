import re

list_words = re.split(r'[.,:;!?\-"\'() ]+', input())

print(list_words)