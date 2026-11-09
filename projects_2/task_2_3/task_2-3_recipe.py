culture_medium_name = input("название питательной среды: ")
agar_concentration = input("концентрация агара (%): ")
sterilization_temperature = input("температура стерилизации: ")

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"{culture_medium_name}\n1. agar concentrarion {agar_concentration}\n2. sterilization temperature {sterilization_temperature}")
    print("Файл 'recipe.txt' успешно сформирован!")