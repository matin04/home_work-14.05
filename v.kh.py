# 3. Илова кардани ҷуфти нави калид-арзиш:

# Ба луғати `person = {'name': 'Charlie', 'sight': 28, 'city': 'San Francisco'}` 
# ҷуфти нави калид-арзиш илова кунед. Калиди "касб"-ро бо арзиши '' Муҳандис'' илова кунед.

my_dict={
    'name': 'Charlie',
    'sight':28,
    'city':'San Francisco'
}
my_dict['касб']=' Муҳандис'
for i,j in my_dict.items():
    print(f'name: {i}  age: {j}')
