choice = input("Запустити калькулятор? (Так/Ні): ")

if choice.lower() == "так":
    expr = input("Введи вираз: ")
    print("Результат:", eval(expr))
elif choice.lower() == "ні":
    print("Програма завершилась.")
else:
    print("Такого варіанта немає. Програма завершилась.")
