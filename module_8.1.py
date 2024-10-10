def add_everything_up(a, b):
    try:
        print(round(a + b, 3))
    except TypeError:
        print(f'{a}{b}')


add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
add_everything_up(123.456, 7)


# Вывод в консоль
# 123.456строка
# яблоко4215
# 130.456