import re

def binary_multiples_of_3(strings):
    pattern = '^(0*(1(01*0)*1)*)*$'  # Регулярное выражение для проверки двоичной записи числа, кратного 3
    result2 = []
    result10 = []
    for s in strings:
        if re.match(pattern, s):
            result2.append(s)
            result10.append(str(int(s,2)))

    return result2, result10

# Пример использования
input_strings = ['1001', '1010', '101001101', '101001100']
result2, result10 = binary_multiples_of_3(input_strings)
print(f'Строки {", ".join(result2)} содержат числа, кратыне 3: {", ".join(result10)}')