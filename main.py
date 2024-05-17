from abc import  ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass
class sword(Weapon):
    def attack(self):
        return "Удар мечом в ближнем бою, урон 2"
    def name(self):
        return "Меч"

class dagger(Weapon):
    def attack(self):
        return "Удар кинжалом в спину, урон 4"

    def name(self):
        return "Кинжал"
class bow(Weapon):
    def attack(self):
        return "Выстрел из лука в дальнем бою, урон 2"
    def name(self):
        return "Лук"

class Fighter():
    def __init__(self, weapon: Weapon):
        self.weapon = weapon
    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"оружие сменено на {self.weapon.name()}")

    def fight(self):
        print(f"боец делает {self.weapon.attack()}")
class Monster():
    pass


sword1 = sword()
bow1= bow()
dagger1 = dagger()
fighter = Fighter(dagger1)
monster = Monster()
fighter.fight()
print("монстр побежден")
fighter.changeWeapon(bow1)
fighter.fight()
print("монстр побежден")
fighter.changeWeapon(sword1)
fighter.fight()
print("монстр побежден")