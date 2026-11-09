produced = float(input("Введите общее количество произведенных капсул: "))
capacity = float(input("Введите количество капсул в одной упаковке: "))

count = int(produced // capacity)
rem = int(produced % capacity)

print('--- Отчет фасовочного цеха ---')
print(f"Полных упаковок:\t{count}")
print(f'Остаток капсул:\t{rem}')