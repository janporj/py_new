future_value = float(input('Введите требуемое будущее значение: '))

rate = float(input('ВВедите годовую процентную ставку: '))

years = int(input('Введите количество лет хранеия денег на счете: '))

present_value = future_value/(1.0 + rate)**years

print('Вам потребуется внести сумму:', present_value)