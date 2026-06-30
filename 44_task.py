def reverse_words(sentence):
    listed_sentence = sentence.split()
    reversed_sentence = reversed(listed_sentence)
    return " ".join(reversed_sentence)

sentence = input().strip()
result = reverse_words(sentence)
print(result)

