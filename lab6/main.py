
arguments = []
fake_arguments = []
matrix = []
final = []

# Проверяем корректность количества критериев
while True:
    try:
        n = int(input('Напишите количество критериев: '))
        break
    except(ValueError, TypeError):
        print('количество может быть только целочисленным')

# Названия критериев
print('Введите названия критериев ')
for i in range(n):
    argument = str(input())
    arguments.append(argument)
    fake_arguments.append(argument)

# Формируем матрицу
for i in range(n):
    string_of_matrix = []
    for j in range(n):
        # удиничная диагональ
        if i == j:
            weight = 1.00
        # ввод первичного веса
        elif i < j:
            print('во сколько аргумент {0} значимее аргумента {1} '.format(fake_arguments[i], fake_arguments[j]))
            while True:
                try:
                    weight = float(input())
                    break
                except(ValueError, TypeError):
                    print('Вы ввели не некорректное значение веса, введите иное ')
        # расчет первичного веса, если имеется обратный
        else:
            weight = float(matrix[j][i]**-1)
        string_of_matrix.append(weight)
    matrix.append(string_of_matrix)

# Считаем сумму матрицы
# (к сожалению, функция sum не работает для матриц/массива массивов, так что приходится считать построчно)
sum_matrix = 0
for i in range(n):
    sum_matrix += sum(matrix[i])
 
# Формируем финальные веса
for i in range(n):
    final.append(float((sum(matrix[i])/sum_matrix)//0.01)/100)

# проверка на ошибки округления
if sum(final) > 100:
    final[final.index(max(final))] -= 1

# Вывод
print(final)
