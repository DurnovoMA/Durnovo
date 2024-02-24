if __name__ == "__main__":
    from typing import Optional


    class Transport:
        """Базовый класс для всех транспортных средств."""

        def __init__(self, brand: str, model: str, year: int):
            """
            Инициализирует объект транспортного средства.

            Аргументы:
            - brand (str): Марка транспортного средства.
            - model (str): Модель транспортного средства.
            - year (int): Год выпуска транспортного средства.
            """
            self.brand = brand
            self.model = model
            self.year = year

        def __str__(self) -> str:
            """Возвращает строковое представление объекта."""
            return f"{self.year} {self.brand} {self.model}"

        def __repr__(self) -> str:
            """Возвращает представление объекта в виде строки."""
            return f"{self.__class__.__name__}(brand={self.brand}, model={self.model}, year={self.year})"

        def refuel(self, fuel_type: str, amount: float) -> str:
            """
            Заправляет транспортное средство определенным типом топлива.

            Аргументы:
            - fuel_type (str): Тип топлива.
            - amount (float): Количество топлива, которое нужно заправить.

            Возвращает:
            - str: Строка с информацией о заправке.
            """
            return f"{self.brand} {self.model} заправлено {amount} литров {fuel_type}."

        def service(self) -> str:
            """
            Обслуживает транспортное средство.

            Возвращает:
            - str: Строка с информацией об обслуживании транспортного средства.
            """
            return f"{self.brand} {self.model} прошло техническое обслуживание."


    class Car(Transport):
        """Класс для представления автомобиля."""

        def __init__(self, brand: str, model: str, year: int, color: Optional[str] = None):
            """
            Инициализирует объект автомобиля.

            Аргументы:
            - brand (str): Марка автомобиля.
            - model (str): Модель автомобиля.
            - year (int): Год выпуска автомобиля.
            - color (Optional[str]): Цвет автомобиля (по умолчанию None).
            """
            super().__init__(brand, model, year)
            self.color = color

        def __str__(self) -> str:
            """Возвращает строковое представление объекта."""
            return f"{super().__str__()}, Цвет: {self.color}"

        def __repr__(self) -> str:
            """Возвращает представление объекта в виде строки."""
            return f"{super().__repr__()}, color={self.color}"

        def service(self) -> str:
            """
            Перегружает метод service для автомобиля.

            Обоснование:
            - Для автомобилей может быть специфическое техническое обслуживание,
              такое как замена рулевых тяг, сайлентблоков и т. д.

            Возвращает:
            - str: Строка с информацией о техническом обслуживании автомобиля.
            """
            return f"{self.brand} {self.model} прошло регулярное техническое обслуживание в автосервисе."

        def start_from_traffic_light(self) -> str:
            """
            Моделирует старт автомобиля со светофора.

            Возвращает:
            - str: Строка с информацией о старте автомобиля со светофора.
            """
            return f"{self.brand} {self.model} начинает движение со светофора."


    class Motorcycle(Transport):
        """Класс для представления мотоцикла."""

        def __init__(self, brand: str, model: str, year: int, engine_capacity: float):
            """
            Инициализирует объект мотоцикла.

            Аргументы:
            - brand (str): Марка мотоцикла.
            - model (str): Модель мотоцикла.
            - year (int): Год выпуска мотоцикла.
            - engine_capacity (float): Объем двигателя мотоцикла.
            """
            super().__init__(brand, model, year)
            self.engine_capacity = engine_capacity

        def __str__(self) -> str:
            """Возвращает строковое представление объекта."""
            return f"{super().__str__()}, Объем двигателя: {self.engine_capacity}"

        def __repr__(self) -> str:
            """Возвращает представление объекта в виде строки."""
            return f"{super().__repr__()}, engine_capacity={self.engine_capacity}"

        def service(self) -> str:
            """
            Перегружает метод service для мотоцикла.

            Обоснование:
            - Для мотоциклов может быть специфическое техническое обслуживание,
              такое как натяжка цепи, смазка амортизаторов и т. д.

            Возвращает:
            - str: Строка с информацией о техническом обслуживании мотоцикла.
            """
            return f"{self.brand} {self.model} прошло плановое техобслуживание в мотосервисе."

        def perform_stunt(self) -> str:
            """
            Выполняет трюк на мотоцикле.

            Возвращает:
            - str: Строка с информацией о выполненном трюке.
            """
            return f"{self.brand} {self.model} выполняет трюк на мотоцикле."
    pass