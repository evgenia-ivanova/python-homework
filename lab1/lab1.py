import re

print('>>> Лабораторну роботу №1 виконала\n'
      '>>> студентка КМ-93 Довгаль Єва\n'
      '>>> Варіанти кожного завдання: 4\n')
print('Суть завдань:\n'
      '      1) Користувач уводить три числа. Збільшити перше число в два рази,\n'
      '       - друге числа зменшити на 3, третє число звести в квадрат\n'
      '       - і потім знайти суму нових трьох чисел.\n'
      '      2) Увести з клавіатури дійсні числа х і у, не рівні одне одному.\n'
      '       - Менше з цих двох чисел замінити половиною їх суми,\n'
      '       - а більше - їх подвоєним добутком.\n'
      '      3) Обчислення конкретної функції, в залежності від введеного значення х.\n')


def validator(pattern, prompt):
    text = input(f'{prompt}: ')
    while not bool(pattern.match(text)):
        text = input(f'{prompt}: ')
    return text


def get_num(prompt, gtype=1):
    re_integer = re.compile('^[-+]?\d+$') if gtype else re.compile('^[-+]?\d*\.\d+$')
    number = int(validator(re_integer, prompt)) if gtype else float(validator(re_integer, prompt))
    return number


def task1():
    print('\n<<< Виконання першого завдання >>>')
    a = get_num('Перше число')
    b = get_num('Друге число')
    c = get_num('Третє число')
    return a * 2 + b - 3 + c ** 2


def task2():
    print('<<< Виконання другого завдання >>>')
    a = b = get_num('Перше число', 0)
    while a == b:
        b = get_num('Друге число', 0)
        if a == b: print('ПОМИЛКА! Змінні x та y не повинні бути рівні одне одному.')
    if a < b:
        return f"x={(a + b) / 2}, y={2 * a * b}"
    else:
        return f"x={2 * a * b}, y={(a + b) / 2}"


def task3():
    print('<<< Виконання третього завдання >>>')
    x = get_num('Введіть значення х')
    return 0 if x <= 1 else round(1.0 / (x + 6.0), 3)


while True:
    choose_task = input('Введіть номер завдання: ').replace(' ', '')
    if choose_task == "1": print(f'Результат виконання першого завдання: {task1()}\n')
    if choose_task == "2": print(f'Результат виконання другого завдання: {task2()}\n')
    if choose_task == "3": print(f'Результат виконання третього завдання: {task3()}\n')
    restart = input('\nПродовжити? Y/N\n').lower()
    if restart != 'y': break
