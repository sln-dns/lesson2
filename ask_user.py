intellect = {
    'привет': 'и Вам здравствуйте.',
    'что делаешь?': 'Программирую',
    'как дела?': 'Отлично!',
    'ты компьютер?': 'я сверхразум!',
    'ответь на главный вопрос жизни, вселенной и всего такого': '42'
}

def ask_user():
         
    while True:
        question = input('Задайте вопрос компьютеру  ')
        question = question.lower()
        if question == 'пока':
            print('и тебе пока')
            break
        else:
            answer = intellect.get(question, 'задайте другой вопрос')
            print(answer)
    
    
    
ask_user()

