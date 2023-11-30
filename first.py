import re

def binary_multiples_of_3(strings):
    pattern = '^(0*(1(01*0)*1)*)*$'  # Регулярное выражение для проверки двоичной записи числа, кратного 3
    result = []
    for s in strings:
        if re.match(pattern, s):
            result.append(s)
    return result

# Пример использования
input_strings = ['1001', '1010', '101001101', '101001100']
result = binary_multiples_of_3(input_strings)
print(result)