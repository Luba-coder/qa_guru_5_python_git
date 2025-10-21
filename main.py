def add(a, b):
    """Сложение двух чисел"""
    return a + b


def subtract(a, b):
    """Вычитание двух чисел"""
    return a - b


def multiply(a, b):
    """Умножение двух чисел"""
    return a * b


def divide(a, b):
    """Деление двух чисел"""
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b


def main():
    print("Простой калькулятор")
    print("Доступные операции: +, -, *, /")

    try:
        num1 = float(input("Введите первое число: "))
        operator = input("Введите оператор (+, -, *, /): ")
        num2 = float(input("Введите второе число: "))

        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            result = "Неверный оператор"

        print(f"Результат: {result}")

    except ValueError:
        print("Ошибка: введите числа корректно")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()