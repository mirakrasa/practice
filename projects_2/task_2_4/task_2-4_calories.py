protein = float(input("protein mass (g): "))
fats = float(input("fats mass (g): "))
carbohydrates = float(input("carbohydrates mass (g): "))

kal = (protein * 4) + (fats * 9) + (carbohydrates * 4)

print(f"Общая калорийность: {kal}")