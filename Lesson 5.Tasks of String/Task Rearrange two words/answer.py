# Условие
# Дана строка, состоящая ровно из двух слов,
# разделенных пробелом. Переставьте эти слова местами.
# Результат запишите в строку и выведите получившуюся строку.
#
# При решении этой задачи не стоит пользоваться циклами и
# инструкцией if.

text = input("Введите текст для перестановки:  ")

c = text.split(' ')
print(' '.join(c[::-1]))
