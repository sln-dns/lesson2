age = int(input('Привет! Сколько тебе лет? '))

def life_path(age):
    if age <= 6:
        return "Ты в яслях или детском саду!"
    elif 7 <= age <= 18:
        return "Привет, школьник!"
    elif 19 <= age <= 22:
        return "Как там в студенчестве?"
    elif 23 <= age <= 65:
        return "Работать и работать!"
    else:
        return "Здравствуй, пенсия!"

occupation = life_path(age)

print(occupation)