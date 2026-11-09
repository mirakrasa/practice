volume = float(input("Введите необходимый объем раствора NaCl: "))

mass_NaCl = round(volume * 0.009, 2)
volume_H2O = volume


with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write('ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:')
    file.write("\n-----------------------")
    file.write(f'\nОбщий объем:\t{volume} мл')
    file.write(f'\nМасса соли:\t{mass_NaCl} г')
    file.write(f'\nОбъем воды:\t{volume_H2O} мл')