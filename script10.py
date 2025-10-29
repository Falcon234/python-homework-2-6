import random

def guess_number_game():
    print("=== Гра: Вгадай число ===")
    print("Я загадав число від 1 до 100. Спробуй його відгадати!")

    random_number = random.randint(1, 100)
    attempts = 0  # лічильник спроб

    while True:
        try:
            guess = int(input("Введи своє число: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Будь ласка, введи число від 1 до 100.")
                continue

            if guess < random_number:
                print("Занадто мало!")
            elif guess > random_number:
                print("Занадто багато!")
            else:
                print(f"🎉 Вітаю, ти вгадав число {random_number} за {attempts} спроб!")
                break

        except ValueError:
            print("Помилка: введи ціле число.")

if __name__ == "__main__":
    guess_number_game()
