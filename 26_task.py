def is_divisible_by_digits(num):
    # Тип int переделываем в список
    listed_number = list(str(num))

    # проходим в цикле по кортежу
    for digit in listed_number:
        # каждый элемент картежа переделываем в int
        digit_int = int(digit)
        # пропускаем ноль, так как деление на ноль невозможно
        if digit_int == 0:
            continue
        # если не делится хотя бы на одну цифру - сразу False
        if num % digit_int != 0:
            return False
    # если все проверки пройдены - True
    return True

number = int(input().strip())
result = is_divisible_by_digits(number)
print(str(result))