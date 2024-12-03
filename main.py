from prompt_toolkit import prompt, PromptSession


score = 0

def has_digit(password):
    global score
    for symbol in password:
        if symbol.isdigit():
            score += 2
            return True
    return False

def is_very_long(password):
    global score
    if len(password) >= 12:
        score += 2
        return True
    return False

def has_letters(password):
    global score
    for symbol in password:
        if symbol.isalpha():
            score += 2
            return True
    return False

def has_upper_letters(password):
    global score
    for symbol in password:
        if symbol.isupper():
            score += 2
            return True
    return False

def has_lower_letters(password):
    global score
    for symbol in password:
        if symbol.islower():
            score += 2
            return True
    return False

def has_symbols(password):
    global score
    for symbol in password:
        if not symbol.isalnum():
            score += 2
            return True
    return False

password = input('Введите пароль: ')

checks = [
    has_digit,
    is_very_long,
    has_letters,
    has_upper_letters,
    has_lower_letters,
    has_symbols,
]
for check in checks:
    check(password)

print('Рейтинг пароля: ' + str(score))


