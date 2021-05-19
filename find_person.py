names = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']

name = 'Валера'
def find_person(name):
    finded_name = names.index(name)
    finded_name = names.pop(finded_name)
    print(f'{finded_name} нашелся')

find_person(name)