class Counter():
    def __init__(self):
        self.count = 0

    def increase(self, value = 1):
            self.count += value

    def decrease(self, value = 1):
            self.count -= value

    def getValue(self):
        return self.count

# Создание счетчика
counter = Counter()
print(counter.getValue())  # Вывод: 0

# Увеличение счетчика
counter.increase()
print(counter.getValue())  # Вывод: 1

# Увеличение счетчика на заданную величину
counter.increase(5)
print(counter.getValue())  # Вывод: 6

# Уменьшение счетчика
counter.decrease()
print(counter.getValue())  # Вывод: 5

# Уменьшение счетчика на заданную величину
counter.decrease(10)
print(counter.getValue())  # Вывод: -5