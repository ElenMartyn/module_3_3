def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(10, 'с конца строка')  # с двумя аргументами
print_params(b = 25)
print_params(c = [1, 2, 3])
print('Ошибку не выдает, но пишет, что надо строку заменять строкой, со списком тоже самое')

values_list = [3.14, 'пример', False] # список
values_dict = {'a': 42, 'b': 'словарь', 'c': None} #словарь

print('Распаковка из списка:')
print_params(*values_list) 
print('Распаковка из словаря:')
print_params(**values_dict)

# Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print("Распаковка списка с отдельными параметрами:")
print_params(*values_list_2, 42)  # распаковка списка и передача отдельного параметра
