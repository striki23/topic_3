hourly_rate = int(input('Введите почасовую ставку: '))  # здесь Ваш код

WORKING_HOURS_PER_DAY = 8
WORKING_DAYS_PER_MONTH = 22

working_hours = WORKING_DAYS_PER_MONTH*\
                WORKING_HOURS_PER_DAY  # здесь Ваш код

salary = hourly_rate*working_hours # здесь Ваш код

print(f'Вы проработали {working_hours} часов')  # допишите код
print(f'Ваша зарплата в месяц: {salary} рублей')  # допишите код
