symbol = input("можно выбрать из следующих действий:\n+ \n- \n// \n* \n** \n% \n:")
total = 0
while True:
    num_1 = int(input("введите первое число:"))
    num_2 = int(input("введите второе число:"))
    if symbol == "+":
        total = num_1 + num_2
        break
    elif symbol == "-":
        total = num_1 - num_2
        break
    elif symbol == "//":
        total = num_1 // num_2
        break
    elif symbol == "*":
        total = num_1 * num_2
        break
    elif symbol == "**":
        total = num_1 ** num_2
        break
    elif symbol == "%":
        total = num_1 % num_2
        break
print(f"Ответ:{total}!")
    
