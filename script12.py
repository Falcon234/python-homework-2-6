data = [
    ["№", "Дата", "Подія"],
    ["1", "10.10", "День народження"]
]

# --- Генератор таблиці ---
def print_table(table):
    # Обчислюємо максимальну ширину кожного стовпця
    col_widths = [max(len(str(row[i])) for row in table) for i in range(len(table[0]))]

    # Створюємо роздільну лінію
    line = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"

    # Виводимо таблицю
    print(line)
    for row in table:
        # Форматуємо кожен рядок у вигляді |  комірка  |  ...
        formatted_row = "| " + " | ".join(f"{str(row[i]):<{col_widths[i]}}" for i in range(len(row))) + " |"
        print(formatted_row)
        print(line)


# --- Виклик функції ---
print_table(data)
