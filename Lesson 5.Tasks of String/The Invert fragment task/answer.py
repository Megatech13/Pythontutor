# Условие
# Дана строка, в которой буква h встречается как минимум
# два раза. Разверните последовательность символов,
# заключенную между первым и последним появлением буквы
# h, в противоположном порядке.
#

text = input('Введите текст:  ')

first_letter = text.find('h')
last_letter = text.rfind('h')

text = text[:first_letter] + text[last_letter:first_letter: -1] + text[last_letter:]

print(text)
