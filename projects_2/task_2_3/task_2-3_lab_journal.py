name = input("ФИО исследователя: ")
date = input("Дата: ")
experiment = input("Название эксперимента: ")
conclusion = input("Вывод: ")

with open("journal.txt", "w", encoding="utf-8") as file:
    file.write("+" + "-" * 60 + "+")
    file.write("\nЭлектронный лабораторный журнал")
    file.write("\n+" + "-" * 60 + "+")
    file.write(f"\nФИО исследователя\t: {name}")
    file.write(f"\nДата\t: {date}")
    file.write(f"\nЭксперимент\t: {experiment}")
    file.write("\n+" + "-" * 60 + "+")
    file.write(f"\nВЫВОД:\n{conclusion}")
    file.write("\n+" + "-" * 60 + "+")

print("Запись в журнале сформирована!")