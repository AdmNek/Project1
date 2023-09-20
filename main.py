print ('Введите число a=')
a = float(input())
print ('Введите число b=')
b = float(input())
print('Выберите операцию')
print('1 - Сложить a + b')
print('2 - Вычесть a - b')
print('3 - Умножить a * b')
print('4 - Разделить a / b')
c = int(input())
match c:
    case 1:
        res = float(a + b)
    case 2:
        res = float(a - b)
    case 3:
        res = float(a * b)
    case 4:
        res = float(a / b)
print(res) 