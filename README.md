# Проект банковского виджета
## Цель проекта
Проект "bank_project" создан для контроля за моей успеваемостью.
С помощью него наставники могут контролировать мой прогресс в обучении.
В конце у меня будет готово собственное приложение.
## Установка
Клонируйте репозиторий
```
git clone https://github.com/RafaelManasyan/bank_project.git
```
## Модуль main.py
В модуле содержится основная функция, которая отвечает за логику всего проекта
## Модуль generators.py
В модуле содержатся три функции, соответственно, для:
1. Фильтрации транзакций по валюте
2. Получения описания по транзакции
3. Генерации номеров для банковских карт

Чтобы постепенно генерировать их вызов необходимо назвать этот вызов переменной и вывести через переменную (на примере filter_by_currency)
```
my_function = filter_by_currency
print(next(my_function(my_list)))
```
## Модуль decorators.py
В модуле содержится декоратор, который позволяет обрабатывать функцию по нужным вам параматерам.
Чтобы использовать декоратор достаточно перед любой функцией иметь запись следующего типа:
```
@decorator_name
```
## Логгеры
В модулях utils.py и masks.py в фукнкциях содержатся логгеры для отображения в отдельном log-файле различной информации по работе данных функций
Логгеры бывают разных уровней: DEBUG, INFO, WARNING, ERROR, CRITICAL
## Чтение xlsx и csv файлов
Для чтения csv-файла необходимо вызвать функцию и указать в нем путь до файла:
```
from_csv_to_py(path)
```
Для чтения csv-файла необходимо вызвать функцию и указать в нем путь до файла:
```
from_xlsx_to_py(path)
```
На выходе в обоих случаях получите список словарей
## Тестирование:
Зайти в терминал и написать следующую команду:
```
pytest
```
Чтобы затем проверить охват тестрирования кода, необходимо прописать следующую командуЖ
```
pytest --cov
```
## Лицензия:
Проект распространяется под [лицензией MIT](LICENSE).
