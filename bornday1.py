year = int(input("В каком году родился А.С Пушкин?:"))
if year == 1799:
    print("Верно!")

    day = int(input("День рождения А.С.Пушкина?:"))
    if day == 26:
        print("День рождения верно!")
    else:
        print("Неверный день рождения!")
else:
    print("Неверный год!")
