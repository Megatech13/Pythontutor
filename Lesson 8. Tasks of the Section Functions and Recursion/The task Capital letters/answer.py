def capitalize(text: str):  # Создаем функцию
    word = text.split() # Генерируем список из строки
    for i in range(len(word)):
        word[i] = word[i].replace(word[i][0], chr(ord(word[i][0]) - 32), 1)
    return (' '.join(word))


print(capitalize(input("Введите текст для обработки:  ")))
