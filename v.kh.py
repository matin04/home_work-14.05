# 2. Дастрасӣ ба арзишҳо:

# Бо назардошти луғат `person = {'name': 'Bob', 'sight': 30, 'city': 'Chicago'}`, дарёфт ва чоп кунед

# арзише, ки бо калиди ''шаҳр'' алоқаманд аст.

my_dict={
    'name': 'Bob',
    'sight':30,
    'city':'Chicago'
}
l=''
for i,j in my_dict.items():
    if i=='city':
        l=j
print(j)
