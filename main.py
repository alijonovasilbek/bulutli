# 10-lik raqamni 16-likka o'tkazish (kutubxonalarsiz)
def decimal_to_hexadecimal(decimal_number):
    if decimal_number == 0:
        return '0'

    hex_digits = '0123456789ABCDEF'
    hexadecimal_number = ''
    while decimal_number > 0:
        hexadecimal_number = hex_digits[decimal_number % 16] + hexadecimal_number
        decimal_number = decimal_number // 16

    return hexadecimal_number


# Versiya 3: 10-likdan 16-likka o'tish
decimal_number = 10
print(f"Versiya 3: {decimal_number} (soni) = {decimal_to_hexadecimal(decimal_number)} (16 likda)")
