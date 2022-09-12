def get_coordinate(input_string):
    while True:
        try:
            num = int(input(input_string))
            return num
        except ValueError:
            print("Неправельный ввод, введите число!")

x1 = get_coordinate("Введите х первой точки: ")
y1 = get_coordinate("Введите y первой точки: ")
x2 = get_coordinate("Введите х второй точки: ")
y2 = get_coordinate("Введите y второй точки: ")

print(f"Расстояние между точкой А({x1},{y1}) и В({x2},{y2}) ровно {round(((x2 - x1)**2 + (y2 - y1)**2)**(1/2), 2)}")