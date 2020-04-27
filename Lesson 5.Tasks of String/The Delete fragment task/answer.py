# Условие
# Дана строка, в которой буква h встречается минимум
# два раза. Удалите из этой строки первое
# и последнее вхождение буквы h, а также все
# символы, находящиеся между ними.

text = input('Введите текст:  ')

first_letter = text.find('h')
last_letter = text.rfind('h')

text = text[:first_letter] + text[last_letter + 1:]

print(text)
