import random as rnd

answers = ['Норм.', 'Лучше всех :)', 'Ну так', 'Отличненько!', 'Ничего, жить буду', 
           'Прекрасно!', 'Замечательно!', 'Как всегда, в порядке!', 'Не могу жаловаться', 'Всё супер!']

def how_are_you():
    return rnd.choice(answers)

print(how_are_you())