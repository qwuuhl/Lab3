'''
Задача №2
Вводяться два чотирицифрових числа a і b.
Виведіть у порядку зростання всі чотирицифрові числа в інтервалі від a до b,
запис яких містить строго три однакові цифри.

Автор: Задворна Анастасія Богданівна
'''

a = int(input("Введіть перше чотирицифрове число a: "))
b = int(input("Введіть друге чотирицифрове число b: "))

print(f"Чотирицифрові числа в інтервалі від {a} до {b}, які містять строго три однакові цифри:")

for num in range(a, b + 1):
    num_str = str(num)
    if len(set(num_str)) == 2 and num_str.count(num_str[0]) == 3:
        print(num)
