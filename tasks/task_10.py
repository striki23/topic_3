name = input('Введите ваше имя: ')  # здесь Ваш код
surname = input('Введите вашу фамилию: ')  # здесь Ваш код
age = int(input('Введите ваш возраст: '))  # здесь Ваш код

# Определите типы данных и идентификаторы в памяти
# Дайте смысловые имена переменным
type_name = type(name)
type_surname = type(surname)
type_age = type(age)
id_name = id(name)
id_surname = id(surname)
id_age = id(age)

# вывод типа и идентификатора каждой переменной
print(f'Тип имени: {type_name}, ID в памяти: {id_name}')  # допишите код
print(f'Тип фамилии: {type_surname}, ID в памяти: {id_surname}')  # допишите код
print(f'Тип возраста: {type_age}, ID в памяти: {id_age}')  # допишите код
