password = input('Введите пароль: ')

if len(password) < 12:
    print("Короткий")
    if password.isdigit():
        print('Цифра')
    else:
        print('Буква')
else:
    print("Длинный")
