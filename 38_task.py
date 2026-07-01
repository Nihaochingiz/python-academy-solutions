def even_chars(s):
    listed_sentence = list(s)
    even_chars = []
    for i,val in enumerate(listed_sentence):
        if i % 2 == 0:
            even_chars.append(val)
    return ''.join(even_chars)


s = 'Hello'
result = even_chars(s)
print(result)