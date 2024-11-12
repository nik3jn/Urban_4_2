def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
test_function()
inner_function()


# вызов inner_function вне функции test_function приводит к ошибке: "NameError: name 'inner_function' is not defined",
# функция inner_function находится внутри функции test_function и получить к ней доступ извне нельзя





