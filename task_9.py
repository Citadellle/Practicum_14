import string

words_dict = {}

word = input().lower().strip(string.punctuation)
while word != '':
    if word not in words_dict:
        words_dict[word] = 1
    else:
        words_dict[word] += 1

    word = input().lower().strip(string.punctuation)

words_dict_sorted = sorted(words_dict.items(),
                           key=lambda i: i[1],
                           reverse=True)

for word in words_dict_sorted:
    print(word[0])
