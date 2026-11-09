weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (см): "))

bmi = round(weight / (height ** 2) * 10**4, 2)

print('--- Отчет о состоянии здоровья ---')
print(f"Рост:\t{height} см")
print(f'Вес:\t{weight} кг')
print(f'Индекс массы тела: {bmi}')