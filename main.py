score = 0
def has_digit(password):
    global score
    for symbols in password:
        if symbols.isdigit():
            score += 2
            return True
    return False

def is_very_long(password):
    global score
    if len(password) < 12:
        return False
    else:
        score += 2
        return True

password = input('Введите пароль: ')

has_digit(password)
is_very_long(password)

print('Рейтинг пароля: ' + str(score))
