import abc
class Entity(abc.ABC):
    def __init__(self, name, max_hp):
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp
    
    @property
    def name(self):
        return self._name
    
    @property
    def hp(self):
        return self._hp
    
    def take_damage(self, dmg):
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0
    def __str__(self):
        return f"{self._name}: {self._hp}/{self._max_hp}"
    @abc.abstractmethod
    def basic_attack(self,opponent):
        pass

    @abc.abstractmethod
    def special_attack(self,opponent):
        pass