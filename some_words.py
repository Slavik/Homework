def single_root_words(root_word, *other_words):
    some_words = []
    for x in other_words:
        if root_word.lower() in x.lower():
            some_words.append(x)
        elif x.lower() in root_word.lower():
            some_words.append(x)
    return some_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)