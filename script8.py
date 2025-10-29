# Програма "Магазин"

def main():
    shop_items = {}  # словник товарів {назва: ціна}
    balance = 0.0    # баланс магазину

    while True:
        print("\n=== МАГАЗИН ===")
        print("1. Додати товар")
        print("2. Видалити товар")
        print("3. Купити товар")
        print("4. Переглянути список товарів")
        print("5. Переглянути баланс магазину")
        print("6. Вихід")

        choice = input("Оберіть дію (1-6): ")

        if choice == "1":
            # Додати товар
            name = input("Введіть назву товару: ").strip()
            if name in shop_items:
                print("Такий товар вже існує.")
                continue
            try:
                price = float(input("Введіть ціну товару: "))
                if price < 0:
                    print("Ціна не може бути від'ємною.")
                    continue
                shop_items[name] = price
                print(f"Товар '{name}' додано з ціною {price:.2f} грн.")
            except ValueError:
                print("Помилка: введіть коректне число для ціни.")

        elif choice == "2":
            # Видалити товар
            name = input("Введіть назву товару для видалення: ").strip()
            if name in shop_items:
                del shop_items[name]
                print(f"Товар '{name}' видалено.")
            else:
                print("Помилка: такого товару немає у списку.")

        elif choice == "3":
            # Купити товар
            name = input("Введіть назву товару для покупки: ").strip()
            if name in shop_items:
                balance += shop_items[name]
                print(f"Ви купили '{name}' за {shop_items[name]:.2f} грн.")
                del shop_items[name]
            else:
                print("Помилка: такого товару немає у магазині.")

        elif choice == "4":
            # Переглянути список товарів
            if not shop_items:
                print("Список товарів порожній.")
            else:
                print("\nДоступні товари:")
                for item, price in shop_items.items():
                    print(f"- {item}: {price:.2f} грн")

        elif choice == "5":
            # Переглянути баланс
            print(f"Поточний баланс магазину: {balance:.2f} грн.")

        elif choice == "6":
            # Вихід
            print("Дякуємо за використання програми 'Магазин'! До побачення!")
            break

        else:
            print("Помилка: оберіть пункт від 1 до 6.")

if __name__ == "__main__":
    main()
