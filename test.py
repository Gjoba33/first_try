def get_data():
    name = input('Введите имя: ')
    age = int(input('Введите город: '))
    city = input('Введите город: ')
    return name, age, city

def show_info(name, age, city):
    print(f"Имя: {name}")
    print(f"Возраст: {age}")
    print(f"Город: {city}")

# Получаем данные из первой функции
name, age, city = get_data()

# Передаем их во вторую функцию
show_info(name, age, city)