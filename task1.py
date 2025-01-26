# У даному випадку, весь код написано за Вас) Ваша ж задача прописати аннотації до функцій.


# ---=============---
def add(num1: int, num2: int) -> int:
    return num1 + num2

print(add(5, 3))
# ---=============---
old_list = ["apple", "pear", "banana"]

def add_element_to_list(lst: list, element: str) -> list:
    lst.append(element)
    return lst

print(add_element_to_list(old_list, "grape"))
# ---=============---
def multiple(num1: float, num2: int) -> float:
    return num1 * num2

print(multiple(5.1, 3))
# ---=============---
def create_list_of_random_numbers(length: int) -> list:
    import random
    lst = []
    for _ in range(length):
        lst.append(random.randint(0, 100))
    return lst

print(create_list_of_random_numbers(10))
# ---=============---