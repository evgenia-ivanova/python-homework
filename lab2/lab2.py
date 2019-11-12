import re

print('>>> Лабораторну роботу №2 виконала\n'
      '>>> студентка КМ-93 Довгаль Єва\n'
      '>>> Варіанти кожного завдання: 4\n')
print('Суть завдань:\n'
      '      1) Сума (x+i)/i по n; i=1\n'
      '      2) Організувати безперервне введення чисел з клавіатури, поки користувач не введе 0.\n'
      '       - Після введення нуля, показати на екрані кількість чисел,\n'
      '       - які були введені, їх загальну суму і середнє арифметичне.\n')


def validator(pattern, prompt):
    text = input(f'{prompt}: ')
    while not bool(pattern.match(text)):
        print('⚠ Помилка! ')
        text = input(f'{prompt}: ')
    return text


def get_num(prompt, gtype=1):
    re_integer = re.compile('^[-+]?\d+$') if gtype else re.compile('^[-+]?\d*(\.\d+)?$')
    number = int(validator(re_integer, prompt)) if gtype else float(validator(re_integer, prompt))
    return number


# Вибирає закінчення для n числа
def end(i: int):
    ending = ['число', 'числа', 'чисел']
    i = str(i)
    if int(i) in range(11, 15): return ending[2]
    elif int(i[-1]) == 1: return ending[0]
    elif int(i[-1]) in range(2, 5): return ending[1]
    else: return ending[2]


def task1():
    print('\n<<< Виконання першого завдання >>>')
    index, result = 1, 0
    x, n = get_num('Значення x'), get_num('Межа сумування')

    for i in range(n):
        result += (x + index) / index
        index += 1
    return float(round(result, 3))


def task2():
    print('\n<<< Виконання другого завдання >>>')
    print('>>>Введеня цілих чисел буде продовжуватися, поки не буде введено 0!')
    entered = []
    while True:
        num = get_num('Введіть число', 0)
        if num == 0:
            if len(entered) == 0:
                print('⚠ Помилка! Треба ввести хоча б одне число.')
                continue
            break
        entered.append(num)
    average = round((float(sum(entered)) / len(entered)), 3)
    print(f'Ви ввели {len(entered)} {end(len(entered))}:\n{entered}\n'
          f'Их сумма: {sum(entered)}. Середнє арифметичне: {average}')


while True:
    choose_task = input('Введіть номер завдання: ').replace(' ', '')
    if choose_task == "1": print(f'Результат виконання першого завдання: {task1()}')
    if choose_task == "2": task2()
    restart = input('\nПродовжити? Y/N').lower()
    if restart != 'y': break