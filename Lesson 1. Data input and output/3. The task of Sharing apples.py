# Условие
# n школьников делят k яблок поровну, неделящийся остаток остается в корзинке.
# Сколько яблок достанется каждому школьнику? Сколько яблок останется в корзинке?
# Программа получает на вход числа n и k и должна вывести искомое количество яблок (два числа).
import time
n = int(input('Введите количество школьников: '))
k = int(input('Введите количество яблок: '))

time.sleep(2)
print('Так так, тебе надо понять как разделить яблоки поровну? И если не поделятся то сколько останется в корзине, '
      'так?...')
time.sleep(1)
answer = input('Можешь ответить ДА или НЕТ, любой другой ответ всё равно не пойму. Давай отвечай скот.... ')
time.sleep(2)
if answer == 'ДА':
    print('Мог и не отвечать, я бы и сам догадался. Ща посчитаю, тут без сто грам не обойтись, Падажи пока')
elif answer == 'НЕТ':
    print('Чё нет то, а чё надо то тебе тогда. Кароч не еби голову. Условие задачи почитай, пжлст. И жди ща посчитаю')
else:
    print('Ну ты дурень, ли "ДА" либо "НЕТ" отвечай. Кароч забей, будем считать что ДА')

time.sleep(2)
print('Жди балять, считаю')
time.sleep(1)
print('В общем так')
time.sleep(1)

if k % n > 0:
    print(f'Тут у каждого представителя школоты будет по {k // n} яблок и в корзине останется {k % n} штук, верно? ')
elif k % n == 0:
    print(f'Тут у каждого представителя школоты будет по {k / n} яблок, а в корзине нихая, вот так вот')