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
            print("Ошибка: введите корректное число!!!!!!")

def main():
    print("Добро пожаловать в продвинутый калькулятор!")

    while True:
        display_menu()
        choice = input("\nВыберите операцию (1-8): ")

        if choice == '8':
            print("До свидания!")
            break

    try:
        if choice in ['1', '2', '3', '4', '5']:
            num1 = get_number("Введите первое число: ")
            num2 = get_number("Введите второе число: ")

            if choice == '1':
                result = add(num1, num2)
                print(f"{num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"{num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"{num1} * {num2} = {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
            elif choice == '5':
                result = power(num1, num2)
                print(f"{num1} ^ {num2} = {result}")

        elif choice == '6':
            num = get_number("Введите число: ")
            result = square_root(num)
            print(f"√{num} = {result}")

        elif choice == '7':
            num = get_number("Введите число: ")
            result = factorial(num)
            print(f"{num}! = {result}")

        else:
            print("Неверный выбор! Попробуйте снова.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()