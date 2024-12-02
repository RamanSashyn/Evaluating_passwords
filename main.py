def contains_digit(password):
    found_digit = "Нет цифр"
    for symbols in password:
        if symbols.isdigit():
            found_digit = "Есть цифры"
            break
    return found_digit

password = input('Введите пароль: ')

if len(password) < 12:
    print("Короткий")
    print(contains_digit(password))
else:
    print("Длинный")
    print(contains_digit(password))
