from Caesar.crypt import Caesar
import string


def _def(ans):
    msg = input("Выберите пункт меню: ")
    if msg not in ans and msg != "out": 
        print("(Неправильно выбран пункт меню, попробуйте еще раз)\n")
        return _def(ans)
    else:
        return msg


def _main():
    print("""Введите цифрой пункт меню:
             1. Шифровать по ключу      
             2. Расшифровать по ключу   
             3. Взломать                """)
    return _def("123")


def _caesar(_msg):
    caesar = None
    rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    rus_extra = string.printable.replace(string.ascii_letters, rus+rus.upper())

    match _msg:
        case "1":
            caesar = Caesar(alpha_map=string.ascii_lowercase)
        case "2":
            caesar = Caesar()
        case "3":
            caesar = Caesar(alpha_map=rus)
        case "4":
            caesar = Caesar(alpha_map=rus_extra)
        case "5":
            caesar = Caesar(alpha_map=rus+string.ascii_lowercase)
        case "6":
            caesar = Caesar(alpha_map=rus+string.printable)
    return caesar


def _first():
    print("\n\n")
    print("""Выберите паттерн шифрования: 
          1. EN
          2. EN + Symbols
          3. RU
          4. RU + Symbols
          5. RU + EN
          6. RU + EN + Symbols
          """)
    caesar = _caesar(_def("123456"))
    msg = input("Введите сообщение: ")
    key = input("Введите ключ: ")
    while not key.isdigit():
        key = input("Введите корректный ключ: ")
    key = int(key)
    return caesar.encrypt(msg, key)


def _second():
    print("\n\n")
    print("""Выберите паттерн шифрования: 
          1. EN
          2. EN + Symbols
          3. RU
          4. RU + Symbols
          5. RU + EN
          6. RU + EN + Symbols
          """)
    caesar = _caesar(_def("123456"))
    msg = input("Введите сообщение: ")
    key = input("Введите ключ: ")
    while not key.isdigit():
        key = input("Введите корректный ключ: ")
    key = int(key)
    return caesar.decrypt(msg, key)


def _third():
    print("\n\n")
    print("""Выберите паттерн шифрования: 
          1. EN
          2. EN + Symbols
          3. RU
          4. RU + Symbols
          5. RU + EN
          6. RU + EN + Symbols
          """)
    caesar = _caesar(_def("123456"))
    msg = input("Введите сообщение: ")
    return caesar.crack(msg)


if __name__ == '__main__':
    print("Приветствую в CaesarCrypt! \n")
    msg = "in"
    while msg != "out":
        msg = _main()
        match msg:
            case "1": 
                print(f"Результат: {_first()} \n")
                msg=input("Enter чтобы продолжить или 'out' без кавычек чтобы выйти ")
            case "2":
                print(f"Результат: {_second()} \n")
                msg=input("Enter чтобы продолжить или 'out' без кавычек чтобы выйти ")
            case "3":
                print(f"Результат: {_third()} \n")
                msg=input("Enter чтобы продолжить или 'out' без кавычек чтобы выйти ")
