def parse(s, t):
    if len(t) != 1: return -1
    if s.count(t) == 0: return -1
    t = s.index(t)
    print(f'{s[:t]} |||| {s[t:]}')


def choose_season(season):
    if season not in range(1, 5): return -1
    print('<<< Виконання першого завдання >>>')
    seasons = ['зима', 'весна', 'лето', 'осень']
    months = [['декабрь', 'январь', 'февраль'],
              ['март', 'апрель', 'май'],
              ['июнь', 'июль', 'август'],
              ['сентябрь', 'октябрь', 'ноябрь']]
    days = [[31, 31, 28], [31, 30, 30], [30, 31, 31], [30, 31, 30]]
    print(f'Ваш сезон - {seasons[season - 1]}\n'
          f'Месяца: {", ".join(months[season - 1])}\n'
          f'Количество дней: {days[season - 1]} (всего: {sum(days[season - 1])})')


for i in range(1, 5): choose_season(i)
while True:
    parse(input('\nВведіть текст: '), input('Введіть 1 символ, після якого розбити строку: '))
    restart = input('Продолжить? Y/N\n')
    if restart.lower() != 'y': break
