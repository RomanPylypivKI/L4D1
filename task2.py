# Створити функцію get_unqiue_numbers яка буде приймати 2 списки з числами і повертати список унікальних чисел у двох списках
# Приклад:
#     ls1 = [1, 2, 3]
#     ls2 = [2, 3, 4]

#     print(get_unqiue_numbers(ls1, ls2)) # Має вивести в консоль [1, 2, 3, 4].
    
# Створити функцію sum_lower_than яка буде приймати ті ж 2 списка і число по якому потрібно вивести лице цифри менші з нього в унікальному списку
# який ви отримаєте з функції get_unqiue_numbers
# Приклад:
#     ls1 = [1, 2, 3]
#     ls2 = [2, 3, 4]
#     not_more = 3
    
#     print(sum_lower_than(ls1, ls2, 3)) # Має вивести в консоль [1, 2, 3]. 

# Обов'язково в функції sum_lower_than викликайте get_unqiue_numbers це і є суть завдання!!!
# Також не забудь будь ласка за Аннотації типів)

import sys # нормально невідображались літери з кирилиці
sys.stdout.reconfigure(encoding='utf-8') # тому додав дані рядки

def get_unqiue_numbers(ls1: list, ls2: list) -> list:
    ls1 += [num for num in ls2 if num not in ls1]
    return ls1

def sum_lower_than(ls1: list, ls2: list, not_more: int) -> list:
    return [num for num in get_unqiue_numbers(ls1, ls2) if num <= not_more]