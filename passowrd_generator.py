from random import choice

def rules():
    print('Привет это генератор паролей')
    print('Далее нужно будет указать длинну пароля и список знаком избегаемых и использоумых')


def get_settings():
    while True:
        
        numbers_of_password = int(input('Ведите количество паролей: '))
        len_pas = int(input('Введите длинну пароля: '))

        used_str = input('Ведите знаки которые будете использовать: ').replace(" ", "")
        no_used_str = input('Ведите знаки которые не будете использовать: ').replace(" ", "")
        
        used_letters = set(used_str)
        no_used_letters = set(no_used_str)

        if used_letters & no_used_letters:
            print('Ошибка: обязательные и необязательные знаки не должны совпадать!')
            print(f'Совподающие символы:' , *used_letters & no_used_letters)
        else:
            print('Проверка проведена успешно')
            return used_letters, no_used_letters, len_pas, numbers_of_password


def create_password(used_letters, no_used_letters, len_pas, numbers_of_password):
    list_used_letters = list(used_letters)
    for i in range (1, numbers_of_password + 1):
        password = [choice(list_used_letters) for _ in range(len_pas) ] 
        print(f'Пароль {i}: {"".join(password)}')
    print('Генерация паролей завершена')


rules()
used_letters, no_used_letters, len_pas, numbers_of_password = get_settings()
create_password(used_letters, no_used_letters, len_pas, numbers_of_password)
