
def number_quarter():
    num = input("Введите номер четверти: ")
    while num.isdigit() is not True:
        print("Ошибка ввода!")
        num = input("Введите число: ")
    num = int(num)
    if num == 1: print("X ∈ (0, +∞), Y ∈ (0, +∞)")
    elif num == 2: print("X ∈ (-∞, 0), Y ∈ (0, +∞)")
    elif num == 3: print("X ∈ (-∞, 0), Y ∈ (-∞ ,0)")
    elif num == 4: print("X ∈ (0, +∞), Y ∈ (-∞ ,0)")
    else: print("Такой четверти не существует")

number_quarter()