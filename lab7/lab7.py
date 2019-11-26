import random

print('>>> Лабораторну роботу №7 виконала\n'
      '>>> студентка КМ-93 Довгаль Єва\n'
      '>>> Варіанти кожного завдання: 4\n')
print('Суть завдання:\n'
      '     Є список з 20 чисел, серед яких є від\'ємні.\n'
      '     Записати кожне від\'ємне число на окремому рядку текстового файлу.\n'
      '     Додатковий список не використовувати.\n')

numbers = []
for i in range(20):
    numbers.append(random.randint(-100, 100))

file = open('negative_numbers.txt', 'w')
print(f'Получен список: {numbers}\n'
      f'Найденные отрицательные числа запишутся в {file.name}, находящийся в директории с лабой.')

for i in range(len(numbers)):
    if numbers[i] < 0:
        file.write(f'{numbers[i]}\n')
    else:
        continue

file.close()
exit()
