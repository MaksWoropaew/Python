# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. 
# При расшифровке происходит обратная операция. К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. 
# "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, 
# которая спрашивает ключ, считывает текст и дешифровывает его.

question = input('Вы хотите зашифровать или дешифровать ваше сообщение? ').upper()
alfha = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
file = open("Python/HomeWork4/file2.txt", "w", encoding="utf-8")

def encryption(alfhabet):
    message = input("Введите сообщение, которое хотите зашифровать: ").upper()
    direction = input("Введите направление сдвига (например, 'вправо'): ")
    number = int(input("Введите шаг сдвига: "))
    new_text = ''
    for i in message:
        place = alfhabet.find(i)
        if direction == 'вправо':
            place_2 = place + number
            if i in alfhabet:
                new_text += alfhabet[place_2]
            else:
                new_text += i
        elif direction == 'влево':
            place_2 = place - number
            if i in alfhabet:
                new_text += alfhabet[place_2]
            else:
                new_text += i
    return new_text

def decryption(alfhabet):
    message = input("Введите сообщение, которое хотите дешифровать: ").upper()
    direction = input("Введите направление сдвига, которое использовали при шифровке (например, 'вправо'): ")
    number = int(input("Введите шаг сдвига: "))
    new_text = ''
    for i in message:
        place = alfhabet.find(i)
        if direction == 'вправо':
            place_2 = place - number
            if i in alfhabet:
                new_text += alfhabet[place_2]
            else:
                new_text += i
        elif direction == 'влево':
            place_2 = place + number
            if i in alfhabet:
                new_text += alfhabet[place_2]
            else:
                new_text += i
    return new_text

if question == 'ЗАШИФРОВАТЬ':
    new_message = encryption(alfha)
    file.write(new_message)
    file.close()
elif question == 'ДЕШИФРОВАТЬ':
    new_message = decryption(alfha)
    file.write(new_message)
    file.close()
else:
    print("ОШИБКА")