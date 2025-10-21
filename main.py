import math

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

def power(a, b):
    """Возведение в степень"""
    return a ** b

def square_root(a):
    """Квадратный корень"""
    if a < 0:
        return "Ошибка: корень из отрицательного числа!"
    return math.sqrt(a)

def factorial(a):
    """Факториал числа"""
    if a < 0:
        return "Ошибка: факториал отрицательного числа!"
    if a == 0:
        return 1
    return math.factorial(int(a))

def display_menu():
    """Отображение меню операций"""
    print("\n" + "="*40)
    print("           ПРОДВИНУТЫЙ КАЛЬКУЛЯТОР")
    print("="*40)
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Возведение в степень (^)")
    print("6. Квадратный корень (√)")
    print("7. Факториал (!)")
    print("8. Выход")
    print("="*40)

def get_number(prompt):
    """Безопасный ввод числа"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число!")

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