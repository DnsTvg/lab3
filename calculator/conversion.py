def km_to_miles(km):
    result = ""
    is_valid, error_message = validate_conversion(km)
    if is_valid:
        result = "{:.3f}".format(km * 0.621371192)

    return result, error_message



def validate_conversion(km):
    try:
        km = float(km)
        if km < 1 or km > 1000:
            return False, "Доступний діапазон значень: 1 ≤ a ≤ 1000, де а - кілометри. "

        return True, ""  # Повертаємо True як позначку успішної валідації
    except ValueError:
        return False, "Введені дані повинні бути числами"
