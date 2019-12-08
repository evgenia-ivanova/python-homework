import tkinter as tk
import numexpr as ne
import numpy as np
import re
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure


VERSION = '0.9.5'
# Понимает, если нарисовано 2 одинаковых графика


WARNING_COLOR = '#F8E0E0'
WHITE = '#FFFFFF'
pi = np.pi
e, exp = np.e, np.e
eps = 0.01
t = np.arange(-5, 5, 0.001)


root = tk.Tk()
root.title(f'РГР: Основи програмування - Python v.{VERSION}')
root.resizable(False, False)

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/2 - windowWidth)
positionDown = int(root.winfo_screenheight()/2 - windowHeight)
root.geometry(f'+{positionRight}+{positionDown}')


# <<< Функции и бинды >>>
def set_results():
    # --> поиск пересечений
    info_results.config(state=tk.NORMAL)
    info_results.delete(0.0, tk.END)

    F1 = ne.evaluate(get_func(entry_1))
    F2 = ne.evaluate(get_func(entry_2))

    X = []
    for x in range(len(t)):
        if np.array_equal(F1, F2): break
        print(f't={t[x]} F1={F1[x]} F2={F2[x]} | {abs(F1[x] - F2[x])} < {eps} => {abs(F1[x] - F2[x]) < eps}')
        if abs(F1[x] - F2[x]) < eps:
            if abs(F1[x] - F2[x]) < abs(F1[x+1] - F2[x+1]) and abs(F1[x] - F2[x]) < abs(F1[x-1] - F2[x-1]):
                X.append([round(t[x], 3), round(F1[x], 3)])
            continue
        else:
            continue

    if np.array_equal(F1, F2):
        print('set_results(): нарисовано два одинаковых графика')
        info_results.insert(tk.INSERT, 'x є R')
    elif len(X) == 0:
        print('set_results(): без пересечений')
        info_results.insert(tk.INSERT, 'Коренів немає')
    else:
        for elem in range(len(X)):
            info_results.insert(tk.INSERT, f'X{elem + 1}: {X[elem]}\n')
            ax.plot(X[elem][0], X[elem][1],  'ro', linewidth=2, markersize=5)
            print(f'X{elem+1}:', X[elem][0], ';', X[elem][1])
    info_results.config(state=tk.DISABLED)


def do_math(func):
    # --> приводит функцию в более подходящий вид для обработки
    func = func.replace(' ', '')
    func = func.replace('y=', '')
    func = func.replace('^', '**')
    func = func.replace('x', 't')
    abs_pattern = re.compile('\|(.+)\|')
    abs_match = re.search(abs_pattern, func)
    if abs_match: func = func.replace(abs_match.group(), f'abs({abs_match.group(1)})')
    return func


def get_func(entry):
    # --> обрабатывает функцию, проверяет, всё ли ок с ней
    if not entry.get():
        entry['bg'] = WARNING_COLOR
        print(f'⚠ ERROR {entry}: функція відсутня')
        return 0

    try:
        entry['bg'] = WARNING_COLOR
        ne.evaluate(do_math(entry.get()))
        entry['bg'] = WHITE
    except KeyError:
        print(f'⚠ ERROR {entry}: допускається лише 1 змінна - \'x\'')
    except ZeroDivisionError:
        print(f'⚠ ERROR {entry}: ділення на нуль')
    except SyntaxError:
        print(f'⚠ ERROR {entry}: помилка в написанні функції')
    except ValueError:
        print(f'⚠ ERROR {entry}: знайдена ін\'єкція :\'(')

    return do_math(entry.get())


def create_graphic(func):
    ax.plot(t, ne.evaluate(func), label=func)


def main_button():
    # --> Так называемая "панель управления"
    get_func(entry_1)
    get_func(entry_2)

    if entry_1['bg'] == WHITE and entry_2['bg'] == WHITE:
        ax.clear()
        ax.grid(True)
        create_graphic(get_func(entry_1))
        create_graphic(get_func(entry_2))
        ax.legend()
        set_results()
        canvas.draw()
    else:
        info_results.config(state=tk.NORMAL)
        info_results.delete(0.0, tk.END)
        info_results.config(state=tk.DISABLED)


# <<< Виджеты блоков и блоки >>>
#   Блок GRAPHIC_FRAME:
GRAPHIC_FRAME = tk.Frame(root)
fig = Figure(figsize=(6, 3.3), dpi=100)
ax = fig.add_subplot(111)
ax.grid(True)
canvas = FigureCanvasTkAgg(fig, GRAPHIC_FRAME)

#   Блок ENTRY_FRAME:
ENTRY_FRAME = tk.Frame(root, bd=2)
entry_1 = tk.Entry(ENTRY_FRAME, bg=WHITE)
entry_2 = tk.Entry(ENTRY_FRAME, bg=WHITE)
build_graphic = tk.Button(ENTRY_FRAME, text='Побудувати', width=15, command=main_button)
root.bind('<Return>', lambda event: main_button())
entry_1.bind('<Control-BackSpace>', lambda event: entry_1.delete(0, tk.END))
entry_2.bind('<Control-BackSpace>', lambda event: entry_2.delete(0, tk.END))

#   Блок RESULT_FRAME:
RESULT_FRAME = tk.Frame(root, bd=2)
tk.Label(RESULT_FRAME, text='Знайдені корені:').grid(row=0)
RESULTS = tk.Frame(RESULT_FRAME)
info_results = tk.Text(RESULTS, height=3.5, width=20, state=tk.DISABLED)
scrollbar = tk.Scrollbar(RESULTS, orient=tk.VERTICAL, command=info_results.yview)
info_results.config(yscrollcommand=scrollbar.set)

#   SIDEBAR_FRAME:
SIDEBAR_FRAME = tk.Frame(root, bd=2)
toolbar = NavigationToolbar2Tk(canvas, SIDEBAR_FRAME)

# <<< Упаковка виджетов >>>
#   GRAPHIC_FRAME:
canvas.get_tk_widget().grid(row=0)

#   ENTRY_FRAME:
build_graphic.grid(row=2, columnspan=2)
tk.Label(ENTRY_FRAME, text='Перша функція: ').grid(row=0, sticky=tk.E)
tk.Label(ENTRY_FRAME, text='Друга функція: ').grid(row=1, sticky=tk.E)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1, pady=5)

#   RESULT_FRAME:
RESULTS.grid(row=1)
info_results.grid(row=0, sticky='wn')
scrollbar.grid(row=0, column=1, sticky='en', ipady=8)

# <<< Упаковка блоков >>>
GRAPHIC_FRAME.grid(row=0, columnspan=2)
ENTRY_FRAME.grid(row=1, column=0, sticky=tk.W, padx=10)
RESULT_FRAME.grid(row=1, column=1, ipady=5)
SIDEBAR_FRAME.grid(row=2, columnspan=2, sticky='we')

# <<< Запуск >>>
root.bind('<Destroy>', exit)
root.mainloop()
