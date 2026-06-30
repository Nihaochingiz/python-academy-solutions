def count_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    s = s.lower()
    listed_sentence = list(s)
    result = 0
    for word in listed_sentence:
        if word in vowels:
            result += 1
    return result



s = input().strip()


result = count_vowels(s)
print(result)