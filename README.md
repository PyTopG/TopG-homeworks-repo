# Домашняя работа

## Описание:

Данная домащняя работа направленная на тестирование различных кейсов при работе с программой.

## Установка:

1.Клонируйте репозиторий:
```
github.com/PyTopG/TopG-homeworks-repo
```
2.Установите зависимости:
```
pip install -r requirements.txt
```

## Использование:

1. Загрузите данные для работы с приложением
2. Для работы приложения воспользуйтесь модулем `main.py`

## Тестирование:

1. Установите фреймворк pytest при помощи команды:
```
poetry add --group dev pytest pytest-cov
```
2. Тестирование проекта осуществляется командой `pytest`
3. Введите команду `poetry run pytest --cov`,чтобы посмотреть покрытие тестами программы

## Тестирование:

1. Установите фреймворк pytest при помощи команды:
```
poetry add --group dev pytest pytest-cov
```
2. Тестирование проекта осуществляется командой `pytest`
3. Введите команду `poetry run pytest --cov`,чтобы посмотреть покрытие тестами программы

# Модуль Транзакций и Генерации Номеров Карт

Этот модуль предоставляет функции для работы с транзакциями и генерации номеров банковских карт.

## Функции

### 1. `filter_by_currency(transactions: list[dict], currency: str = "USD") -> Optional[dict]`
Возвращает первую транзакцию с заданной валютой или `None`, если такой транзакции нет.

#### Пример:
```python
result = filter_by_currency(transactions, "USD")
```
### 2. `transaction_descriptions(transactions: list[dict]) -> Iterator[str]`
Возвращает описания транзакций.
#### Пример:
```python
for description in transaction_descriptions(transactions):
    print(description)
```

### 3. `card_number_generator(start: int = 0, stop: int = 9999999999999999) -> Iterator[str]`
Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX.
#### Пример:
```python
for card_number in card_number_generator(0, 5):
    print(card_number)
```

### Лицензия
Лицензия MIT.


