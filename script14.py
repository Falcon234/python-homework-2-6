def hello():
    name = input("Введи своє ім'я: ")
    print(f"Привіт, {name}!")


def is_even(n):
    if n % 2 == 0:
        print("Парне")
    else:
        print("Непарне")


def min_num(a, b, c):
    return min(a, b, c)


is_even(2) 
is_even(3)  
print(min_num(1, 2, 3))  # 1
