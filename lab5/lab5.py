print('>>> Лабораторну роботу №5 виконала\n'
      '>>> студентка КМ-93 Довгаль Єва\n'
      '>>> Варіанти кожного завдання: 4\n')
print('Суть завдання:\n'
      '      1) Створити два списки, однакових за кількістю слів. Необхідно:\n'
      '       - порівняти слова на однакових позиціях і видалити більше;\n'
      '       - якщо слова однакові по довжині, видалити обидва;\n'
      '       - вивести на екран обидва модифікованих списку.\n'
      '      2) F=((A+B)∩(A∪B))')

def get_int(faq: str):
    while True:
        try:
            num = int(input(f'{faq}: '))
            break
        except ValueError:
            print('ПОМИЛКА! Вводити потрібно лише цілі числа.')
    return num


def create_list(len):
    new_list = []
    for i in range(len):
        new_list.append(input(f' Елемент {i+1}: '))
    print(f'Отримано список: {new_list}')
    return new_list


def task1():
    print('\n<<< Виконання першого завдання >>>')
    list_len = get_int('Введіть кількість слів у списках')

    print('Введіть перший список:')
    list1 = create_list(list_len)
    print('Введіть другий список:')
    list2 = create_list(list_len)

    rem1, rem2 = [], []
    for i in range(len(list1)):
        if len(list1[i]) > len(list2[i]):
            rem1.insert(0, i)
        elif len(list1[i]) < len(list2[i]):
            rem2.insert(0, i)
        else:
            rem1.insert(0, i)
            rem2.insert(0, i)

    for i in range(len(rem1)): list1.pop(rem1[i])
    for i in range(len(rem2)): list2.pop(rem2[i])

    print(f'1: {list1}\n2: {list2}')


def task2():
    print('\n<<< Виконання другого завдання >>>')
    A = {1, '2', 'ee', 'a', 'd'}
    B = {'d', 'ee', 4, 3}
    print(f'((A+B)∩(A∪B)) = {((A ^ B) & (A | B))}')


# Списки для завдання 1:
first_list = ['hello', 'hello', 'WorlD@', 'd', 'EVAEVA', 'nul1l', 'TEST!!!!']
second_list = ['d', 'ee', 'adssadsa', 'ssssss', 'EVAEVA', '2', 'TEST!!!!']
# Запуск завдань:
task1()
task2()
