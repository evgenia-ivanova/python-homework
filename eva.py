def repl(obj):
    for_repl = [',', '.', ':', ';', '!', '?']
    for i in range(len(for_repl)):
        obj.replace(for_repl[i], '')
    return obj.replace('-', ' ')


def count_words(obj):
    counter = []
    for i in range(len(obj)):
        counter.append(obj.count(i))
    return counter


def min_words(obj):
    pass

text = repl(input('Your text: ').lower()).split()
count_words(text)
print(min_words(text))

