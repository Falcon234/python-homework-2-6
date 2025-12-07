class Human:
    def __init__(self):
        self.name = "Микита"
        self.age = 15
        self.hobbies = ["програмування", "ігри", "музика"]
        self.superpower = "швидко вчитися новому"
        self.energy = 100

    def introduce(self):
        return (
            f"Привіт! Я {self.name}, мені {self.age} років. "
            f"Я люблю {', '.join(self.hobbies)} і маю суперсилу — {self.superpower}."
        )

    def code(self):
        if self.energy >= 20:
            self.energy -= 20
            return "💻 Я пишу код і стаю ще розумнішим!"
        else:
            return "😴 Потрібна підзарядка."

    def rest(self):
        self.energy = min(100, self.energy + 30)
        return "🔋 Я відпочив і відновив енергію!"


# Приклад використання
person = Human()
print(person.introduce())
print(person.code())
print(person.rest())
print("Енергія:", person.energy)
