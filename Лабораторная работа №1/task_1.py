# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import doctest
class Car:
    """
    Класс, представляющий из себя машину с её характеристиками
    """
    def __init__(self, RWheel: Union[int, float], Power:int, People:int):
        """

        :param RWheel: радиус колеса
        :param Power: мощность двигателя
        :param People: количество людей в машине

        Примеры:
        >>> car1 = Car(16.5, 120, 5)
        """
        if not RWheel > 0:
            raise ValueError("Радиус колеса не может быть отрицательным числом")
        if not isinstance(RWheel, (int, float)):
            raise TypeError("Радиус колеса может быть только целым или с плавающей запятой")
        self.RWheel = RWheel

        if not Power > 0:
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
    def ludi(self, person: int) -> int:
        """

        :param person: изменяемое количество человек в машине
        :return: новое количество человек в машине
        """
        ...

class Bottle:
    """
    Класс, представляющий из себя, бутылку с водой в мл
    """
    def __init__(self, ml: int, ml_ism: int):
        """

        :param ml: Объем бутылки в МЛ
        :param ml_ism: Объем оставшейся жидкости в бутылке

        Примеры:
        >>> bottle = Bottle(300, 100)
        """
        if not ml > 0:
            raise ValueError("Миллилитраж - должно быть положительное число ")
        if not isinstance(ml, int):
            raise TypeError("Миллилитраж бутылки должно быть только целое число")
        self.ml = ml

        if not ml_ism >= 0:
            raise ValueError("Миллилитраж - должно быть положительное число ")
        if not isinstance(ml_ism, int):
            raise TypeError("Миллилитраж бутылки должно быть только целое число")
        self.ml_ism = ml_ism

    def is_empty_bottle(self) -> bool:
        """
        Функция которая проверяет является ли бутылка пустой
        :return: Является ли бутылка пустой (Правда или Ложь)

        Примеры:
        >>> bottle = Bottle(500,0)
        >>> bottle.is_empty_bottle()

        """
        ...

    def add_water_to_bottle(self, water: int) -> None:
        """
        Добавление воды в стакан.
        :param water: Объем добавляемой жидкости
        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в бутылке, то вызываем ошибку

        Примеры:
        >>> bottle = Bottle(500, 0)
        >>> bottle.add_water_to_bottle(200)
        """
        if not isinstance(water, int):
            raise TypeError("Добавляемая жидкость в мл должна быть целым числом")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна положительным числом")
        ...

class BankAccount:
    """
    Класс, представляющий банковский счет.
    """
    def __init__(self, account_holder: str, balance: float):
        """

        :param account_holder: Имя владельца счета
        :param balance: Баланс счета в рублях
        """
        if not isinstance(account_holder, str):
            raise TypeError("Держатель аккаунта должен быть с типом данных строка")
        self.account_holder = account_holder

        if not isinstance(balance, str):
            raise TypeError("Баланс карты должен быть числом с плавающей запятой")
        self.balance = balance

    def open_account(self, account_holder: str) -> None:
        """
        Открывает новый банковский счет.
        :param account_holder: Имя владельца счета
        :return: Новый счет в банке
        """
        ...

    def deposit(self, amount: float) -> float:
        """

        :param amount: Сумма для внесения на счет
        :return: Новая сумма на счету
        """
        if not amount >= 0:
            raise ValueError("Сумма - должно быть положительное число")
        if not isinstance(amount, int):
            raise TypeError("Сумма должна быть числом с плавающей запятой")
        ...

if __name__ == "__main__":
    doctest.testmod()
    pass
