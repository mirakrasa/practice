operator_name = input("operator name: ")
pressure = input("current pressure sensor value: ")

with open("sensor_log.txt", "w", encoding="utf-8") as file:
    file.write("OPERATOR\tVALUE\n")
    file.write(f"{operator_name}\t{pressure}\n")
    print("Данные успешно сохранены в sensor_log.txt")