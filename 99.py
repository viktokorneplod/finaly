from random import *

a = list(map(int, input('Введите сколько угодно чисел через пробел').split()))
print('sum:', sum(a))
print('dif:', a[0] - sum(a[1:len(a)]))


print('sos')
print(randint(1, 6))
print('The end')

