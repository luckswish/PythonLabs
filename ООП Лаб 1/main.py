import doctest
from typing import Union


class Student:
    def __init__(self, lastname: str, age: int, stipend: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Студент"

        :param lastname: Фамилия студента
        :param age: Возраст студента
        :param stipend: Стипендия

        Примеры:
        >>> student = Student('Иванов', 18, 2000)  # инициализация экземпляра класса
        """
        if not isinstance(lastname, str):
            raise TypeError("Фамилия должна быть типа str")
        if len(lastname) < 1:
            raise ValueError("Фамилия должна содержать хотя бы один символ")
        self.lastname = lastname

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if age <= 0:
            raise ValueError("Возраст должен быть положительным числом")
        self.age = age

        if not isinstance(stipend, (int, float)):
            raise TypeError("Стипендия должна быть типа int или float")
        if stipend < 0:
            raise ValueError("Стипедния не может быть меньше нуля")
        self.stipend = stipend

    def is_adult(self) -> bool:
        """
        Метод, который проверяет является ли студент совершеннолетним

        :return: Является ли студент совершеннолетним

        Примеры:
        >>> student = Student('Иванов', 18, 2000)
        >>> student.is_adult()
        """
        ...

    def increase_stipend(self, growth: Union[int, float]) -> None:
        """
        Метод, увеличивающий стипендию студента
        :param growth: Размер прибавки к стипендии

        Примеры:
        >>> student = Student('Иванов', 18, 2000)
        >>> student.increase_stipend(1500)
        """
        if not isinstance(growth, (int, float)):
            raise TypeError("growth должно быть типа int или float")
        ...

    def decrease_stipend(self, reduction: Union[int, float]) -> None:
        """
        Метод, уменьшающий стипендию студента
        :param reduction: Величина, на которую уменьшают стипендию
        :raise ValueError: Если величина, на которую уменьшают стипендию превышает стипендию студента,
        то возвращается ошибка.

        Примеры:
        >>> student = Student('Иванов', 18, 2000)
        >>> student.decrease_stipend(1000)
        """
        if not isinstance(reduction, (int, float)):
            raise TypeError("reduction должно быть типа int или float")
        ...


class Car:
    def __init__(self, model: str, current_mileage: Union[int, float], last_inspection_mileage: Union[int, float],
                 release_year: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param model: Модель авто
        :param current_mileage: Текущий пробег
        :param last_inspection_mileage: Пробег на последнем ТО
        :param release_year: Год выпуска авто

        Примеры:
        >>> car = Car('BMW G20', 16750.3, 7504.8, 2022)  # инициализация экземпляра класса
        """
        if not isinstance(model, str):
            raise TypeError("Модель авто должна быть типа str")
        if len(model) < 1:
            raise ValueError("Модель должна содержать хотя бы один символ")
        self.model = model

        if not isinstance(current_mileage, (int, float)):
            raise TypeError("Пробег должен быть типа int или float")
        if current_mileage < 0:
            raise ValueError("Пробег не может быть меньше нуля")
        self.current_mileage = current_mileage

        if not isinstance(last_inspection_mileage, (int, float)):
            raise TypeError("Пробег должен быть типа int или float")
        if last_inspection_mileage < 0:
            raise ValueError("Пробег не может быть меньше нуля")
        if last_inspection_mileage > current_mileage:
            raise ValueError("Пробег на последнем ТО не может быть больше текущего")
        self.last_inspection_mileage = last_inspection_mileage

        if not isinstance(release_year, int):
            raise TypeError("Год должен быть типа int")
        if release_year < 1886:
            raise ValueError("Год выпуска должен быть не ранее 1886")
        self.release_year = release_year

    def is_need_to_change_oil(self) -> bool:
        """
        Метод, позволяющий узнать пора ли менять масло в двигателе

        :return: Нужно ли менять масло в двигателе

        Примеры:
        >>> car = Car('BMW G20', 16750.3, 7504.8, 2022)
        >>> car.is_need_to_change_oil()
        """
        ...

    def calculate_approximate_cost(self) -> float:
        """
        Метод, рассчитывающий примерную стоимость авто,
        основываясь на пробеге и годе выпуска и модели.

        :return: Примерная стоимость авто

        Примеры:
        >>> car = Car('BMW G20', 16750.3, 7504.8, 2022)
        >>> car.calculate_approximate_cost()
        """
        ...


class LocalNetwork:
    def __init__(self, max_num_of_computers: int, connected_computers: int, speed: float):
        """
        Создание и подготовка к работе объекта "Локальная сеть"

        :param max_num_of_computers: Максимальное число компьютеров для подключения
        :param connected_computers: Число подключенных компьютеров
        :param speed: Скорость передачи данных (Мбит/с)

        Примеры:
        >>> net = LocalNetwork(20, 10, 10.5)# инициализация экземпляра класса
        """
        if not isinstance(max_num_of_computers, int):
            raise TypeError("Максимальное число компьютеров должно быть типа int")
        if max_num_of_computers <= 0:
            raise ValueError("Максимальное число компьютеров должно быть положительным")
        self.max_num_of_computers = max_num_of_computers

        if not isinstance(connected_computers, int):
            raise TypeError("Число подключенных компьютеров должно быть типа int")
        if connected_computers < 0:
            raise ValueError("Число подключенных компьютеров не может быть меньше нуля")
        if connected_computers > max_num_of_computers:
            raise ValueError("Число подключенных компьютеров не может превышать максимальное "
                             "число компьютеров для подключения")
        self.connected_computers = connected_computers

        if not isinstance(speed, float):
            raise TypeError("Скорость должна быть типа float")
        if speed < 0:
            raise ValueError("Скорость не может быть меньше нуля")
        self.speed = speed

    def add_computers(self, number_of_computers: int) -> None:
        """
        Добавление компьютеров в локальную сеть
        :param number_of_computers: Число компьютеров, которые нужно добавить

        :raise ValueError: Если сума числа компьютеров, которые нужно добавить и числа уже
        подключенных компьютеров превышает максимально доступное число компьютеров для подключения

        Примеры:
        >>> net = LocalNetwork(20, 10, 10.0)
        >>> net.add_computers(3)
        """
        if not isinstance(number_of_computers, int):
            raise TypeError("Число компьютеров должно быть типа int")
        if self.connected_computers + number_of_computers > self.max_num_of_computers:
            raise ValueError("Сумма подключенных и подключаемых компьютеров должна быть меньше"
                             "максимально доступного числа компьютеров для подключения")
        ...

    def calculate_file_transfer_time(self, file_weight: float) -> float:
        """
        Расчет времени передачи файла, заданного размера по сети
        :param file_weight: Размер файла
        :return: Рассчетное время передачи файла (с)

        Примеры:
        >>> net = LocalNetwork(20, 10, 10.0)
        >>> net.calculate_file_transfer_time(5.0)
        """
        if not isinstance(file_weight, float):
            raise TypeError("Размер файла должен быть типа float")
        ...


if __name__ == "__main__":
    doctest.testmod()
