from abc import ABC, abstractmethod

# Шаг 1: Создайте абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализуйте конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Удар мечом в ближнем бою, урон 2"

class Bow(Weapon):
    def attack(self):
        return "Выстрел из лука в дальнем бою, урон 2"

class Dagger(Weapon):
    def attack(self):
        return "Удар кинжалом в спину, урон 4"

# Шаг 3: Модифицируйте класс Fighter
class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon

    def fight(self):
        print(f"Боец наносит {self.weapon.attack()}")

# Класс Monster
class Monster:
    def __init__(self):
        print("Монстр вступает в бой")

# Шаг 4: Реализация боя
def main():
    # Создаем оружие
    sword = Sword()
    bow = Bow()
    dagger = Dagger()

    # Создаем бойца с начальным оружием
    fighter = Fighter(dagger)
    monster = Monster()

    # Первый бой
    fighter.fight()
    print("Монстр побежден!\n")

    # Меняем оружие и проводим следующий бой
    fighter.changeWeapon(bow)
    fighter.fight()
    print("Монстр побежден!\n")

    # Меняем оружие и проводим следующий бой
    fighter.changeWeapon(sword)
    fighter.fight()
    print("Монстр побежден!\n")

if __name__ == "__main__":
    main()