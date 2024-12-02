password = input('Введите пароль: ')

if len(password) < 12:
    print("Короткий")
    for symbols in password:
        if symbols.isdigit():
            print(symbols + ' - Цифра')
        elif symbols.isalpha():
            print(symbols + ' - Буква')
else:
    print("Длинный")
