my_dict = {'Kit': 1997, 'Tanya': 2001, 'Valya': 1981}
print(my_dict)
print(my_dict['Valya'])
print(my_dict.get('Ira'))
my_dict['Ira'] = 1985
my_dict['Oleg'] = 1983
a = my_dict.pop('Kit')
print(a)
print(my_dict)

my_set = {525, 0, 523, 0, 242, 0, 525}
print(my_set)
print(my_set.add(35))
print(my_set.add(15))
print(my_set.discard(525))
print(my_set)