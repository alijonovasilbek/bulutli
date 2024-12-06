# def decimal_to_binary(decimal_number):
#     if decimal_number == 0:
#         return '0'
#
#     binary_number = ''
#     while decimal_number > 0:
#         binary_number = str(decimal_number % 2) + binary_number
#         decimal_number = decimal_number // 2
#
#     return binary_number
#
#
# # Versiya 1: 10-likdan 2-likka o'tish
# decimal_number = 10
# print(f"Versiya 1: {decimal_number} soni = {decimal_to_binary(decimal_number)} ikkilikda")


# 10-lik raqamni 8-likka o'tkazish (kutubxonalarsiz)
def decimal_to_octal(decimal_number):
    if decimal_number == 0:
        return '0'

    octal_number = ''
    while decimal_number > 0:
        octal_number = str(decimal_number % 8) + octal_number
        decimal_number = decimal_number // 8

    return octal_number


# Versiya 2: 10-likdan 8-likka o'tish
decimal_number = 10
print(f"Versiya 2: {decimal_number} (soni) = {decimal_to_octal(decimal_number)} ( 8 likda)")

