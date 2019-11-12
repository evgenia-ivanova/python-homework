def task():
    print('\n<<< Виконання завдання >>>')
    # Получаем строку и сразу разбираем её по словам в массив (список) через split()
    # Строка "привет всем и пока" в split сделает список: ['привет', 'всем', 'и', 'пока']
    text = input('Введіть щось: ').split()
    # Перебираем каждое слово:
    # Создаём типо последовательность от 0 до длинны списка (нашей строки, которая теперь список)
    # Длинна списка будет 4, но максимальный индекс = 3 (потому что нумерация от нуля)
    for i in range(len(text)):
        # Если первая буква (вторая кв. скобочка [0]) равна 'a', то
        if text[i-1][0].lower() == 'a':
            # Если длина слова <= 3, то оно нафиг удаляется, а цикл начинает новую итерацию (continue)
            if len(text[i-1]) <= 3:
                text.pop(i-1)
                continue
            # Бахаем срез этому слову ([:-3] означает от первого символа до 3-го с конца (за конец отвечает минус))
            text[i-1] = text[i-1][:-3]
    # " ".join(список) собирает весь список в строку с разделителем " " (пробелы, но можно хоть " *** ")
    print(f'    Результат: {" ".join(text)}')


print('\n>>> Лабораторну роботу №3 виконала\n'
      '>>> студентка КМ-93 Довгаль Єва\n'
      '>>> Варіанти кожного завдання: 4\n')
print('Суть завдання:\n'
      '    Видалити останні 3 символа зі слів, що починаються на "a"')

while True:
    task()
    restart = input('Може ще раз? Y/N\n')
    if restart.lower().replace(' ', '') != 'y': break
