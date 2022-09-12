def number_float():
    while type:
        number_float = input()
        try:
            number_float = float(number_float)
        except ValueError:
            print("Неверный ввод, введите число!!!")
        else:
            break
    return number_float

def get_point_local (x_point, y_point):
    if x_point == 0:
        print("Эта точка находится на оси Y!")
    elif y_point == 0:
        print("Эта точка находится на оси X!")
    elif x_point == 0 and y_point == 0:
        print("Это точка пересечения координат!")
    elif x_point > 0 and y_point > 0:
        print("Эта точка находится в I четверти координат!")
    elif x_point < 0 and y_point > 0:
        print("Эта точка находится в II четверти координат!")
    elif x_point < 0 and y_point < 0:
        print("Эта точка находится в III четверти координат!")
    else:
        print("Эта точка находится в IV четверти координат!")

print("Введите координату X : ")
x = number_float()
print("Введите координату Y : ")
y = number_float()
get_point_local(x,y)


