# try:
#     numerator = float(input("Enter the numerator: "))
#     denominator = float(input("Enter the denominator: "))
#
#     if denominator == 0:
#         raise ZeroDivisionError("Division by zero is not allowed")
#
#     result = numerator / denominator
#     print("The result is: ", result)
#
# except ZeroDivisionError as e:
#     print("Error:", e)


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



# Перша версія без обробки винятків усередині функції
# def divide_numbers(a, b):
#     result = a / b
#     print("Результат ділення: ", result)
#
# try:
#     num1 = float(input("Введіть перше число: "))
#     num2 = float(input("Введіть друге число: "))
#     divide_numbers(num1, num2)
# except ZeroDivisionError:
#     print("Ділення на нуль неможливе")
# except ValueError:
#     print("Будь ласка, введіть числа")


# Друга версія з обробкою винятків усередині функції
# def divide_numbers(a, b):
#     try:
#         result = a / b
#         print("Результат ділення: ", result)
#     except ZeroDivisionError:
#         print("Ділення на нуль неможливе")
#
# try:
#     num1 = float(input("Введіть перше число: "))
#     num2 = float(input("Введіть друге число: "))
#     divide_numbers(num1, num2)
# except ValueError:
#     print("Будь ласка, введіть числа")

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# try:
#     apples = int(input("Enter a apple u have: "))
#     if apples < 0:
#         raise Exception("як ти можеш мати яблук менше нуля?!!?")
#     part_numbers = int(input("Enter number of parts: "))
#     part_amount = apples / part_numbers
# except (ZeroDivisionError, ValueError):
#     print("Куда ділиш і що вводиш в цифру, АЛООООООООООО")
# except Exception as ex:
#     print(ex)
# except:
#     print("bite")
# finally:
#     print("The program done")

# ..............................................................


def fill_dictionary():
    dictionary = {}

    while True:
        key = input("Enter key (press Enter to exit): ")
        if not key:
            break
        value = input("Enter value: ")
        dictionary[key] = value

    return dictionary


def display_menu():
    print("Menu:")
    print("1. Display dictionary")
    print("2. Search for value in dictionary")
    print("3. Display value for key")
    print("4. Delete value for key")
    print("5. Exit")


def display_dictionary(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")


def search_value(dictionary):
    value = input("Enter value to search for: ")
    keys = [key for key, val in dictionary.items() if val == value]

    if keys:
        print(f"Keys with value '{value}': {', '.join(keys)}")
    else:
        print(f"Value '{value}' not found in dictionary")


def display_value_for_key(dictionary):
    key = input("Enter key to display value: ")
    value = dictionary.get(key, "Key not found in dictionary")
    print(f"Value for key '{key}': {value}")


def delete_value_for_key(dictionary):
    key = input("Enter key to delete value: ")

    try:
        del dictionary[key]
        print(f"Value for key '{key}' deleted successfully")
    except KeyError:
        print(f"Key '{key}' not found in dictionary. Unable to delete value.")


if __name__ == "__main__":
    my_dictionary = fill_dictionary()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            display_dictionary(my_dictionary)
        elif choice == "2":
            search_value(my_dictionary)
        elif choice == "3":
            display_value_for_key(my_dictionary)
        elif choice == "4":
            delete_value_for_key(my_dictionary)
        elif choice == "5":
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")
