my_dict = {'Kit': 1997, 'Tanya': 2001, 'Valya': 1981}
print('Словарь my_dickt:', my_dict)
print('Год рождения Вали:', my_dict['Valya'])
print('Год рождения Иры:', my_dict.get('Ira'))
my_dict['Ira'] = 1985
my_dict['Oleg'] = 1983
del_key = my_dict.pop('Kit') # убрали ключ 'Kit'
print('Удаленная Кит:', del_key)
print('Новый словарь my_dickt:', my_dict)

my_set = {525, 0, 523, 0, 242, 0, 525}
print('Множество:', my_set)
my_set.add(35) # добавление 35
my_set.add(15) # добавление 15
my_set.discard(525) #удаление без ошибки 525
print('Модифицированное множество my_set:', my_set)
