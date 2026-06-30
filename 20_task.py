def min_amplitude(arr):
    # Если элементов мало, можно сделать амплитуду 0
    if len(arr) <= 4:
        return 0

    # Сортируем массив
    arr.sort()
    n = len(arr)

    # Можно изменить до 3 элементов, значит убираем k элементов слева и 3-k справа
    # Перебираем все варианты: (0,3), (1,2), (2,1), (3,0)
    min_amp = float('inf')

    for left in range(4):  # сколько убрать слева
        right = 3 - left  # сколько убрать справа
        # Оставшийся отрезок массива
        current_amp = arr[n - 1 - right] - arr[left]
        min_amp = min(min_amp, current_amp)

    return min_amp


arr = [4, -8, -1, 3, 7, 10, 5]
print(min_amplitude(arr))  # 4