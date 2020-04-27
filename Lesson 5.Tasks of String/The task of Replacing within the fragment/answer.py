# Условие
# Дана строка. Замените в этой строке все появления буквы
# h на букву H, кроме первого и последнего вхождения.
#

text = input('Введите текст:   ')
first_letter = text.find('h')
last_letter = text.rfind('h')

print(
    text[:first_letter + 1] +
    text[first_letter + 1:last_letter].replace('h', 'H') +
    text[last_letter:]
)
