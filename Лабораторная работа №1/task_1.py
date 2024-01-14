# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import doctest
class Car:
    def __init__(self, RWheel: Union[int, float], Power:int, People:int):
        """

        :param RWheel: радиус колеса
        :param Power: мощность двигателя
        :param People: количество людей в машине

        >>> car1 = Car(16.5, 120, 5)
        """
        if not RWheel > 0
            raise ValueError("Радиус колеса не может быть отрицательным числом")
        if not isinstance(RWheel, (int, float)):
            raise TypeError("Радиус колеса может быть только целым или с плавающей запятой")
        self.RWheel = RWheel

        if not Power > 0
            raise ValueError("Мощность машины не может быть отрицательным числом")
        if not isinstance(Power, int):
            raise TypeError("Мощность машины должна быть целым числом")
        self.Power = Power

        self.People = People

    # метод увеличения мощности двигателя на значение PowerUP
    def Chip(self, PowerUP: int)-> int:
        """

        :param PowerUP: значение увеличения мощности
        :return: новое значение мощности (Power+PowerUP)
        """
        ...

    # метод изменения радиуса колеса на значение Wheel
    def Koleso(self, Wheel: Union[int, float]) ->  Union[int, float]:
        """

        :param Wheel: значение на которое меняется радиус колеса
        :return: новый радиус колеса
        """
        ...

    # метод изменения человек в машине
    def ludi(self, person:int) -> int:
        """

        :param person: изменяемое количество человек в машине
        :return: новое количество человек в машине
        """
        ...

if __name__ == "__main__":
    doctest.testmod()
    pass
