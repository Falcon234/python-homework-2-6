def create_sword():
    return create_weapon(
        name="Короткий меч",
        description="Легкий меч для швидких атак",
        damage=10
    )


def create_axe():
    return create_weapon(
        name="Бойова сокира",
        description="Важка сокира для потужних ударів",
        damage=14
    )


def create_dagger():
    return create_weapon(
        name="Кинджал",
        description="Малий, але дуже небезпечний",
        damage=7
    )


def create_bow():
    return create_weapon(
        name="Лук",
        description="Саморобний лук з міцною тятивою",
        damage=9
    )


def create_fire_staff():
    return create_weapon(
        name="Вогняний посох",
        description="Магічний посох, що випускає полум’я",
        damage=16
    )
  def create_iron_helmet():
    return create_armor(
        name="Залізний шолом",
        description="Голова буде цілою...",
        defense=3,
        piece="helmet"
    )


def create_iron_chestplate():
    return create_armor(
        name="Залізний нагрудник",
        description="Тяжкий нагрудник з кованого заліза",
        defense=6,
        piece="chestplate"
    )


def create_iron_leggings():
    return create_armor(
        name="Залізні штани",
        description="Залізні поножі для захисту самого головного",
        defense=4,
        piece="leggings"
    )


def create_iron_boots():
    return create_armor(
        name="Залізні чоботи",
        description="Важкі чоботи з заліза",
        defense=2,
        piece="boots"
    )
  def create_magic_helmet():
    return create_armor(
        name="Магічний шолом",
        description="Наповнений захисними чарами",
        defense=4,
        piece="helmet"
    )


def create_magic_chestplate():
    return create_armor(
        name="Магічний нагрудник",
        description="Легка, але міцна магічна броня",
        defense=7,
        piece="chestplate"
    )


def create_magic_leggings():
    return create_armor(
        name="Магічні поножі",
        description="Покращують рухи власника",
        defense=5,
        piece="leggings"
    )


def create_magic_boots():
    return create_armor(
        name="Магічні чоботи",
        description="Дають швидкість та захист",
        defense=3,
        piece="boots"
    )
def create_weak_blob():
    blob = create_person("Слабкий слайм")
    blob["stats"]["health"] = 25
    blob["stats"]["strength"] = 1
    blob["stats"]["agility"] = 10
    blob["stats"]["intelligence"] = 0
    blob["stats"]["level"] = 2
    return blob


def create_dark_knight():
    knight = create_person("Темний лицар")
    knight["stats"]["health"] = 80
    knight["stats"]["strength"] = 12
    knight["stats"]["agility"] = 5
    knight["stats"]["intelligence"] = 3
    knight["stats"]["level"] = 8
    return knight
