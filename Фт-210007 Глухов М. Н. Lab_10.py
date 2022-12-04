money = [64, 32, 16, 8, 4, 2, 1]
banknotes = []
number_of_banknotes = 0

while True:
    try:
        summ = int(input('Введите сумму '))
        assert summ > 0
        break
    except ValueError:
        print('Некорректный ввод, введите натуральное число.')
    except AssertionError:
        print('Число должно быть больше 0.')


print('Будут купюры номиналом: ')
temp = summ//64
summ = summ - (temp*64)
print('По 64 - ', temp)
temp = summ//32
summ = summ - (temp*32)
print('По 32 - ', temp)
temp = summ//16
summ = summ - (temp*16)
print('По 16 - ', temp)
temp = summ//8
summ = summ - (temp*8)
print('По 8 - ', temp)
temp = summ//4
summ = summ - (temp*4)
print('По 4 - ', temp)
temp = summ//2
summ = summ - (temp*2)
print('По 2 - ', temp)
temp = summ//1
summ = summ - (temp*1)
print('По 1 - ', temp)