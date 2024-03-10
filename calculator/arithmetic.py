def calculate(number1, number2, operation):
    result = ""
    is_valid, error_message = validate_values(number1, number2, operation)
    if is_valid:
        result = "{:.3f}".format(eval(str(number1) + str(operation) + str(number2)))

    return result, error_message




def validate_values(number1, number2, operation):
    try:
        number1 = float(number1)
        number2 = float(number2)

        print("перше")
        # Перевірка чи знаменник не дорівнює нулю
        if operation == "/" and number2 == 0:
            return False, "Знаменник не може бути рівним нулю"
        print("друге")
        return True, ""  # Повертаємо True як позначку успішної валідації
    except ValueError:
        return False, "Введені дані повинні бути числами"
