from abc import ABC, abstractmethod
from datetime import datetime as DateTime
from typing import Protocol

class BeingLiving(ABC):
    def __init__(self, birth_date: DateTime | None = None):
        self._birth_date: DateTime | None = birth_date
        self._death_date: DateTime | None = None
    
    def birth(self):
        self._birth_date = DateTime.now()

    def die(self):
        self._death_date = DateTime.now()

class AbleToCommunicate:
    @abstractmethod
    def communicate(self): ...
    
class AbleToMove:
    @abstractmethod
    def move(self, x: float, y: float): ...

    @abstractmethod
    def get_current_location(self) -> tuple[float, float]: ...
    
class Wildlife(BeingLiving, AbleToCommunicate, AbleToMove, ABC): # Wildlife(BeingLiving, Bidule)
    def __init__(self):
        super().__init__(birth_date=DateTime.now())
        # BeingLiving.__init__(self, birth_date=DateTime.now())
        # Bidule.__init__(self)
        self._birth_date = None
        self._current_location: tuple[float, float] = None

    def get_current_location(self) -> tuple[float, float]:
        return self._current_location

    def move(self, x: float, y: float):
        self._current_location = (x, y)

class AbleToMeow(Protocol):
    @abstractmethod
    def meow(self): ...

class Cat(Wildlife, AbleToMeow):
    def __init__(self, name: str):
        super().__init__()
        self.__name: str = name
    def meow(self):
        print("Miaou")

    def communicate(self):
        self.meow()

class AbleToBark(Protocol):
    @abstractmethod
    def bark(self): ...

class Dog(Wildlife, AbleToBark):
    def __init__(self, name: str):
        super().__init__()
        self.__name: str = name
    
    def bark(self):
        print("Ouaf ouaf !")

    def communicate(self):
        self.bark()

class Rooster(Wildlife):
    def __init__(self, name: str):
        super().__init__()
        self.__name: str = name
    
    def communicate(self):
        print("Coco Rico")
    

animal = Cat("Nala")
animal.communicate()
