def has_digit(password):
    return any(symbol.isdigit() for symbol in password)


def is_very_long(password):
    return len(password) >= 12


def has_letters(password):
    return any(symbol.isalpha() for symbol in password)


def has_upper_letters(password):
    return any(symbol.isupper() for symbol in password)


def has_lower_letters(password):
    return any(symbol.islower() for symbol in password)


def has_symbols(password):
    return any(not symbol.isalnum() for symbol in password)


def calculate_score(password):
    score = 0

    checks = [
        has_digit,
        is_very_long,
        has_letters,
        has_upper_letters,
        has_lower_letters,
        has_symbols,
    ]

    for check in checks:
        if check(password):
            score += 2

    return score


password = input("Введите пароль: ")
print(f"Рейтинг пароля: {calculate_score(password)}")
