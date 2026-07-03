def is_happy_number(number):
    str_num = str(number)
    length = len(str_num)

    if length % 2 != 0:
        return False

    half = length // 2

    first_half = str_num[:half]
    second_half = str_num[half:]


    product_first = 1
    for digit in first_half:
        product_first *= int(digit)

    product_second = 1
    for digit in second_half:
        product_second *= int(digit)

    return product_first == product_second

number = int(6262)
result = is_happy_number(number)
print(result)