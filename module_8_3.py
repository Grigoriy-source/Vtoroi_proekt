class Car:
    def __init__(self, model: str, vin: int, numbers: str):
        self.model = model  # название автомобиля(строка)
        if self.__is_valid_vin(vin):
            self.__vin = vin  # vin номер автомобиля(целое число)
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers  # номера автомобиля (строка)

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif len(str(vin_number)) != 7:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

def createCar(model: str, vin: int, numbers: str) -> Car:
    try:
        first = Car('Model1', 1000000, 'f123dj')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')

    try:
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    try:
        third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')


if __name__ == '__main__':
    first = createCar('Model1', 1000000, 'f123dj')
    second = createCar('Model2', 300, 'т001тр')
    third = createCar('Model3', 2020202, 'нет номера')