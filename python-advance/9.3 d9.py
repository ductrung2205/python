import re
def password_check(password):
    #calculating the length
    length_error = len(password) <= 8
    #searching for digits
    digit_error = re.search(r"\d", password) is None
    #searching for uppercase
    uppercase_error = re.search(r"[A-Z]", password) is None
    #searching for lowercase
    lowercase_error = re.search(r"[a-z]", password) is None
    #searching for symbols
    symbol_error = re.search(r"[!@#$%^&*]"+r'"]', password) is None

    password_ok = not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error)

    return {
        'password_ok': password_ok,
        'length_error': length_error,
        'digit_error': digit_error,
        'uppercasae_error': uppercase_error,
        'lowercase_error': lowercase_error,
        'symbol_error': symbol_error
    }

    