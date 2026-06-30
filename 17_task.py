current_text = 'Radar'

def is_palindrome(text):
    chars = list(text.lower())
    reversed_chars = list(reversed(chars))
    return chars == reversed_chars

print(is_palindrome(current_text))

# input_text = input().strip()
# result = is_palindrome(input_text)
# print(result)