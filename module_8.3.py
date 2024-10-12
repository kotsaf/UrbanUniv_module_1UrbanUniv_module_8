class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model
        if self.__is_valid_vin(__vin) and self.__is_valid_numbers(__numbers):
            self.__vin = __vin
            self.__numbers = __numbers

    def __is_valid_vin(self, vin):
        if not isinstance(vin, int):
            raise IncorrectVinNumber('Некорректный тип vin номерa')
        elif len(str(vin)) != 7:
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
        super().__init__(message)


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        super().__init__(message)



try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc)
except IncorrectCarNumbers as exc:
    print(exc)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc)
except IncorrectCarNumbers as exc:
    print(exc)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc)
except IncorrectCarNumbers as exc:
    print(exc)
else:
    print(f'{third.model} успешно создан')
