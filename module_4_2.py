

def test_function():

    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


def test():
    try:
        inner_function()
    except Exception as e:
        print(e)

    test_function()


if __name__ == '__main__':    test()


"""
2023/10/24 00:00|Домашняя работа по уроку "Пространство имен."
Домашнее задание по уроку "Пространство имен"

Создайте новый проект в PyCharm
Запустите созданный проект
Ваша задача:
Создайте новую функцию test_function
Создайте внутри test_function другую функцию - inner_function, Эта функция должна печатать значение "Я в области видимости функции test_function"
Вызовите функцию inner_function внутри функции test_function
Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы
Файл с кодом module_4_2.py загрузите на GitHub репозиторий и пришлите ссылку на него.
"""