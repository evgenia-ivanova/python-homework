def repl(obj):
    for_repl = [',', '.', ':', ';', '!', '?']
    for i in range(len(for_repl)):
        obj = obj.replace(for_repl[i], '')
    return obj.replace('-', ' ')


def count_words(obj):
    counter = []
    unique_words = list(set(obj))
    for i in range(len(unique_words)):
        counter.append(obj.count(unique_words[i]))
    return [unique_words, counter]


def min_words(obj):
    unicount = count_words(obj)
    minimal = min(unicount[1])
    right_words = []
    for i in range(len(unicount[0])):
        if unicount[1][i] == minimal: right_words.append(unicount[0][i])
    return ' '.join(right_words)


text = repl(input('Your text: ')).lower().split()
print(min_words(text))
