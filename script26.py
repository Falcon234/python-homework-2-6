class Planet:
    def __init__(self, name, radius, distance_from_sun):
        self.name = name
        self.radius = radius
        self.distance_from_sun = distance_from_sun

    def info(self):
        return f"Планета {self.name}: радіус {self.radius} км, відстань від Сонця {self.distance_from_sun} млн км"

    def orbit_time(self):
        return self.distance_from_sun * 10


# Дочірні класи планет
class Mercury(Planet):
    def __init__(self, radius, distance_from_sun):
        super().__init__("Меркурій", radius, distance_from_sun)


class Venus(Planet):
    def __init__(self, radius, distance_from_sun):
        super().__init__("Венера", radius, distance_from_sun)


class Earth(Planet):   # (у тебе було Earch, але правильно Earth)
    def __init__(self, radius, distance_from_sun):
        super().__init__("Земля", radius, distance_from_sun)


class Mars(Planet):
    def __init__(self, radius, distance_from_sun):
        super().__init__("Марс", radius, distance_from_sun)


class Jupiter(Planet):
    def __init__(self, radius, distance_from_sun):
        super().__init__("Юпітер", radius, distance_from_sun)


class Saturn(Planet):
    def __init__(self, radius, distance_from_sun):
        super().__init__("Сатурн", radius, distance_from_sun)


class Uranus(Planet):
    def __init__(self, radius, distance_from_sun):
        super().__init__("Уран", radius, distance_from_sun)


class Neptune(Planet):
    def __init__(self, radius, distance_from_sun):
        super().__init__("Нептун", radius, distance_from_sun)


# Приклад використання
earth = Earth(6371, 149.6)
print(earth.info())
print("Час оберту:", earth.orbit_time(), "днів")
