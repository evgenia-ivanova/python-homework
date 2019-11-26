import numpy as np

print('>>> Лабораторну роботу №6 виконала\n'
      '>>> студентка КМ-93 Довгаль Єва\n'
      '>>> Варіанти кожного завдання: 4\n')
print('Суть завдання:\n'
      '      1) Дан одновимірний масив числових значень, що нараховує n елементів.\n'
      '         Поміняти місцями групу з m елементів, що починаються з позиції k\n'
      '         з групою з m елементів, що починаються з позиції p.\n'
      '      2) Виконати обробку елементів прямокутної матриці A, що має n рядків і m стовпців.\n'
      '         Знайти найменше значення серед середніх значень для кожного рядка матриці\n')


def get_num(faq, param=0, gtype=int, expected=0):
    errors = ('невід\'ємні', 'більші за 0', 'більші за 1')
    type_error = {int: 'цілі', float: 'дійсні'}
    while True:
        try:
            num = gtype(input(f'{faq}: '))
            if param and num < param-1:
                print(f'⚠ Помилка! За умовою можна вводити лише {errors[param-1]} {type_error[gtype]} числа.')
                continue
            if expected and not(0 < num < expected):
                print(f'⚠ Помилка! За умовою можна вводити лише менші за {expected} {type_error[gtype]} числа.')
                continue
            break
        except ValueError:
            print(f'⚠ Помилка! Вводити можна лише {type_error[gtype]} числа.')
    return num


def task1():
    A, numbers = [], []
    n = get_num('Введіть кількість елементів', 3)
    for i in range(n):
        A.append(get_num(f'{i}', gtype=float))
    print(f'>>> Отримано: {A}')

    print('\n   ▸ Кількість елементів перестановки < загальної кіль-ті елементів'
          '\n   ▸ Позиції елементів < кількість елементів перестановки\n')
    s_elems = get_num('Введіть кількість елементів перестановки', expected=n)
    first_pos = get_num('Введіть позицію цих елементів', expected=n-s_elems+2)-1
    second_pos = get_num('Введіть позицію елементів, з якими міняємося місцями', expected=n-s_elems+2)-1
    print(f'    m: {s_elems}, k: {first_pos}, p: {second_pos}\n    {A}')


def task2():
    A, means = [], []
    n = get_num('Введіть кількість рядків', 2)
    m = get_num('Введіть кількість стовпців', 2)

    for i in range(n):
        A.append([])
        for elem in range(m):
            A[i].append(get_num(f'{i + 1}.{elem + 1}', gtype=float))
    print('\nОтримана матриця:\n', np.array(A))
    for i in range(n): means.append(np.mean(A[i]))

    print(f'Найменше середнє арифметичне на {means.index(min(means)) + 1} рядку: {min(means)}.')


while True:
    choose_task = input('Введіть номер завдання ("1" чи "2"): ').replace(' ', '')
    if choose_task == '1':
        while True:
            task1()
            restart = input('Продовжити? Y/N\n')
            if restart.lower() != 'y': break
        continue
    if choose_task == '2':
        while True:
            task2()
            restart = input('Продовжити? Y/N\n')
            if restart.lower() != 'y': break
        continue
    if choose_task.lower() == 'stop': break
    print('Для завершення програми введіть "stop".')
