def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return '0'

    binary_number = ''
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number = decimal_number // 2

    return binary_number


# Versiya 1: 10-likdan 2-likka o'tish
decimal_number = 10
print(f"Versiya 1: {decimal_number} soni = {decimal_to_binary(decimal_number)} ikkilikda")
