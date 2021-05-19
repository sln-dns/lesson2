
def hello_user():
    
    while True:
        user_say = input('Как дела? ')
        if user_say.lower() == 'хорошо':
            print('и у меня хорошо')
            break
        else:
            print(f'А точно {user_say}, может ещё подумаешь?')


hello_user()