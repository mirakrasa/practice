phenotype_d = input("Введите фенотип группы крови донора (I, II, III, IV): ").strip().upper()
phenotype_r = input("Введите фенотип группы крови реципиента (I, II, III, IV): ").strip().upper()
if phenotype_d == phenotype_r or phenotype_d == "I":
    print("Переливание возможно")
else:
    print("Переливание не возможно")