
# user_num, user_num_day = int(input("введите общий бюджет поездки:")), int(input("введите количество дней поездки:"))
# user_money_tiket, user_money_hostel = int(input("введите цену билетов:")), int(input("введите цену на отель:"))
# user_day = int(input("введите количество дней:"))
# user_sum_day = int(input(f"введите бюджет на траты в течении {user_day} дней:"))
# total_1 = user_num * user_num_day
# total_2 = user_money_tiket + user_money_hostel 
# total_3 = user_sum_day // user_day
# total_4 = user_sum_day % user_day
# if total_1 < 10000:
#     print(total_1, total_2, total_3, total_4)
# else:
#     print("Проверь бюджет поездки")
print("Калькулятор путешественника:")
print("1.)посчитать стоимость общего бюджета\n2.) посчитать стоимость на билеты\n3.)бюджет на несколько дней".capitalize())
total = 0
select = int(input("здесь можно посчитать общий бюджет поездки,расход на отели и авиабилеты, бюджет на несколько дней\nвыберите действие:"))
while True:
    if select == 1:
        num_1 = int(input("введите количество дней:"))
        num_2 = int(input("стоимость:"))
        summ = num_1 * num_2
        print(f"сумма общего бюджета = {summ}")
        if summ > 10000:
            print("Проверь бюджет проездки.")
            break
        else:
            break
    elif select == 2:
        num_1 = int(input("введите стоимость отеля:"))
        num_2 = int(input("введите стоимость авиабилета:"))
        print(f"сумма общего бюджета = {num_1 + num_2}")
        break
    elif select == 3:
        num_1 = int(input("введите количество дней:"))
        num_2 = int(input("введите бюджет на 1 день:"))
        print(f"сумма общего бюджета = {num_1 * num_2}")
        break
    else:
        print("что-то введено не так")
        break

