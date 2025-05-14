# 8. Словарь из двух списков:

# Имея два списка, `keys = ['name', 'age', 'city']` и `values ​​= ['Grace', 35, 'Seattle']`, 
# создайте словарь, объединив эти списки.


keys = ['name', 'age', 'city']
values = ['Grace', 35, 'Seattle']
my_dict = dict(zip(keys, values))
print(my_dict)


