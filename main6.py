# #№1
# text = input()
# print(text.upper())
# #№2
# text = input()
# text_2 = text.lower
# if text_2 == "НЕТ" or text_2 == "ДА":
#     print("отклонено")
# else:
#     print("Принято")
# №3
# text = input()
# print(text.capitalize())
#№4
# text = input()
# print(text.swapcase())
#№5
#text = input()
#print(text.strip())

#№6
# text = input()
# print(text.lstrip())
#№7
# text = input()
# print(text.rstrip())

# while True:
#     num = [4]
#     num_input = int(input())
#     resylt = num * num_input
#     print(resylt)
    
# a = ["яблоко", "чипсы" ,"хлеб" ,"бананы" ,"коквкола"]
# for element in a:
#     if element == "бананы":
#         print("в списке есть бананы")
# items = ["футболка" ,"книга" ,"мяч" ,"бутылка" ,"ключи" ,"телефон"]
# has_phone = False
# for item in items:
#     if item == 'телефон':
#         has_phone = True
# if has_phone:
#     print('в рюкзаке лежит телефон')
# else:
#     print("проверь есть ли телефон в рюкзаке")           



# tem = [-10, 20, -21, 30, 1, -2, 9, -5, 13, 42]
# has_anamaly = False
# for anomaly in tem:
#     if tem < 10 or tem > 35:
#         has_anamaly = True
#         break
# if has_anamaly == True:
#     print("обнаружена аномалия")
# else:
#     print("температура в норме")
# lesson = ['мяч', 'учебник англиского','данные от аккаунта soundcloud', 'ручка', 'карандаш']
# has_book = False
# for intem in lesson:
#     if intem == "учебник англиского":
#         has_book = True
#         print(" есть учебник англиского")
#     else:
#         print("нету")
#     break

# def frict(sweet):
#     return f"фрукт {sweet}"

# print(frict)
# print(frict("сладкий"))




# num = int(input())
# a = []
# for element in range(num):
#     a.append(int(input()))
#     min_vaule = a[0]
#     print(*a)
#     if element < min_vaule:
#         min_vaule = element
#     print(min_vaule)



# n = int(input())
# a = []
# for i in range(n):
#         a.append(int(input()))
#         ind_max = 0
# for eleme in range(len(a)):
#         if a[eleme] > a[ind_max]:
#                 ind_max = eleme
# print(a)
# print(ind_max)  
#               
# num = int(input())
# name = []
# name_found = False
# for i in range(num):
#         name.append(input())
# for eleme in name:
#         a = input()
#         if eleme == a:
#                 name_found = True
#                 print("ДА")
#         else:
#                 print("НЕТ")


# num = int(input())
# a = []
# for i in range(num):
#         a.append(int(input()))
#         ind_max = 0
#         ind_min = 0
# for k in range(len(a)):
#         if a[k] > a[ind_max]:
#                 ind_max = k
#         if a[k] < a[ind_min]:
#                 ind_min = k
# a[ind_max], a[ind_max] = a[ind_min], a[ind_max]
# print(a)

# num = int(input())
# name = []
# name_found = False
# for i in range(num):
#         name.append(input())
# for eleme in name:
#         a = input()
#         if eleme == a:
#                 name_found = True
#                 print("ДА")
#         else:
#                 name_found = False
#                 print("НЕТ")