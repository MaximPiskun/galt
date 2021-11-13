import telebot
#from config import API_TOKEN
from random import randint


bot = telebot.TeleBot("")
controller = {}

def makeX():
    return randint(1, 100)
def makeI(X):
    return randint(1, X)
def makeY():
    return randint(1, 1000)


@bot.message_handler(commands=['start'])
def start_message(message):
    global x123
    global i123
    global balls123
    x123 = makeX()
    i123 = makeI(x123)
    balls123 = makeY()
    bot.send_message(message.from_user.id,"Есть доска Гальтона с основанием ", x123,". Сколько шариков окажется в ",i123 ,"клетке, если всего будет выброшено ",balls123, "шариков? ")
    user_id = message.from_user.id
    controller[user_id] = 'start'
def pascal(x1):
    r = [1]
    for i in range(x1):
        row = [sum(x) for x in zip([0] + row, row + [0])]
    return row
def simulate(x,balls,i):
    j = pascal(x)
    summ = sum(j)
    k = j[i-1]
    c = 0
    for i in range(balls):
        z = randint(1, summ)
        if z <= k:
            c = c + 1


@bot.message_handler(content_types=['text'])
def start(message):
    user_id = message.from_user.id
    user_choice = message.text
    user_state = controller.get(user_id, 'start')
    if user_state == 'start':
        answer = start_handler(user_id, user_choice)

def start_handler(user_id, user_choice):
    g = simulate(x123,balls123,i123)
    return " Вы ошиблись на",g/user_choice,"%"










