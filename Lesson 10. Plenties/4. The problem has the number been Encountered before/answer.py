# Условие
# Во входной строке записана последовательность чисел через пробел.
# Для каждого числа выведите слово YES (в отдельной строке),
# если это число ранее встречалось в последовательности или NO, если не встречалось.
#


a = [int(i) for i in input().split()]
# вводим список строк и переводим в список чисел используя генератор
b = set(a)
# преобразуем полученный список в множество
for i in range(len(a)):
    if a[i] in b:  # определяем вхожения элемента списка в множество, если есть то удаляем его из множества
        print('NO')
        b.remove(a[i])
    else:
        print('YES')  # так как первичное вхождение удалено, следующего такого же  не будет
