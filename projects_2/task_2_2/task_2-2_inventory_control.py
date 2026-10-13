new_reagent_name = input("Введите название нового реактива: ")
new_reagent_amount = input("Введите количество нового реактива: ")

f = open("projects_2/task_2_2/inventory.txt", "w", encoding="utf-8")

print(f"Реактив {new_reagent_name} поступил на склад в количестве {new_reagent_amount} шт.", file=f)
f.close()