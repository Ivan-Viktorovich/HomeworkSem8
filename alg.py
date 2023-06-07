from func import create
from interface import interface
path = "phone_book.txt"
create(path)
enter = 0
while enter != 4:
    enter = interface()
    if enter == 1:
        from func import add_cont
        stroka = str(input("Введите ФИО и номер телефона через пробел "))
        add_cont(path, stroka)
    elif enter == 2:
        from func import show_all
        print(show_all(path))
    elif enter == 3:
        from func import search
        stroka = str(input("Введите фамилию "))
        search(path, stroka)
    elif enter == 5:
        from func import transformation
        from func import add_cont
        stroka = str(input("Введите фамилию для изменения "))
        transformation(path, stroka)
        add_cont(path, stroka)
        

print("спасибо за работу")