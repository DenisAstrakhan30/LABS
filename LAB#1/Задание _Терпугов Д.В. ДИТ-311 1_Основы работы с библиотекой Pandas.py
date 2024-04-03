print('Задание №1')
import pandas as pd
# Чтение файла и сохранение в переменной df
df = pd.read_csv('C:/Users/denis/Desktop/Программирвание для анализа данных/1_Основы работы с библиотекой Pandas ✓/student-mat.csv')
# Вывод первых 10 строк таблицы
print(df.head(10))
# Сохранение размеров таблицы
shape_table = df.shape
# Вывод размера таблицы
print("Размер таблицы:", shape_table)
# Получение количества наблюдений из переменной shape_table
observations_table = shape_table[0]
# Вывод количества наблюдений
print("Количество наблюдений:", observations_table)
# Получение числа наблюдений из информации о таблице
observations_info_table = df.shape[0]
# Проверка совпадения количества наблюдений
if observations_info_table == observations_table:
    print("Решение верно, количество наблюдений равно", observations_table)
else:
    print("Решение неверно, проверьте ещё раз!")

print()
print('Задание №2')
import pandas as pd
# предположим, что у нас есть DataFrame data с колонками Medu и Fedu
data = pd.read_csv('C:/Users/denis/Desktop/Программирвание для анализа данных/1_Основы работы с библиотекой Pandas ✓/student-mat.csv')
parents = data[['Medu', 'Fedu']]
# Вывод первых 20 строк
print(parents.head(20))
# Подсчет числа матерей со средним образованием
mother_high = len(parents[parents['Medu'] == 4])
# Печать результата
print("Число матерей с высшим образованием равно", mother_high)
# Подсчет числа отцов со средним образованием
father_high = len(parents[parents['Fedu'] == 4])
# Печать результата
print("Число отцов с высшим образованием равно", father_high)
# Сравнение значений и вывод информации о победителе
if mother_high > father_high:
    print("Победитель: матери")
elif mother_high < father_high:
    print("Победитель: отцы")
else:
    print("Ничья")


