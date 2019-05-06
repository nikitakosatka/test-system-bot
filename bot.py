from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler
from random import shuffle
import json
import logging

logging.basicConfig(level=logging.DEBUG)

with open("test.json", "rt", encoding="utf8") as f:
    test = json.loads(f.read())['test']


def start(bot, update, user_data):
    shuffle(test)
    update.message.reply_text(
        "Это тест по истории, состоящий из 10 перемешанных вопросов\n"
        "Вы можете прервать тест, послав команду /stop.\n"
        "{}".format(test[0]['question']))

    return 1


def first_response(bot, update, user_data):
    if update.message.text != test[0]['response']:
        update.message.reply_text(f'Неверно. Правильный ответ: {test[0]["response"]}')
        user_data['right_answers'] = 0
    else:
        update.message.reply_text('Верно!')
        user_data['right_answers'] = 1

    update.message.reply_text(
        "{}".format(test[1]['question']))
    return 2


def second_response(bot, update, user_data):
    if update.message.text != test[1]['response']:
        update.message.reply_text(f'Неверно. Правильный ответ: {test[1]["response"]}')
    else:
        update.message.reply_text('Верно!')
        user_data['right_answers'] += 1

    update.message.reply_text(
        "{}".format(test[2]['question']))
    return 3


def third_response(bot, update, user_data):
    if update.message.text != test[2]['response']:
        update.message.reply_text(f'Неверно. Правильный ответ: {test[2]["response"]}')
    else:
        update.message.reply_text('Верно!')
        user_data['right_answers'] += 1

    update.message.reply_text(
        "{}".format(test[3]['question']))
    return 4


def fourth_response(bot, update, user_data):
    if update.message.text != test[3]['response']:
        update.message.reply_text(f'Неверно. Правильный ответ: {test[3]["response"]}')
    else:
        update.message.reply_text('Верно!')
        user_data['right_answers'] += 1

    update.message.reply_text(
        "{}".format(test[4]['question']))
    return 5


def fifth_response(bot, update, user_data):
    if update.message.text != test[4]['response']:
        update.message.reply_text(f'Неверно. Правильный ответ: {test[4]["response"]}')
    else:
        update.message.reply_text('Верно!')
        user_data['right_answers'] += 1

    update.message.reply_text(
        "{}".format(test[5]['question']))
    return 6


def sixth_response(bot, update, user_data):
    if update.message.text != test[5]['response']:
        update.message.reply_text(f'Неверно. Правильный ответ: {test[5]["response"]}')
    else:
        update.message.reply_text('Верно!')
        user_data['right_answers'] += 1

    update.message.reply_text(
        "{}".format(test[6]['question']))
    return 7


def seventh_response(bot, update, user_data):
    if update.message.text != test[6]['response']:
        update.message.reply_text(f'Неверно. Правильный ответ: {test[6]["response"]}')
    else:
        update.message.reply_text('Верно!')
        user_data['right_answers'] += 1

    update.message.reply_text(
        "{}".format(test[7]['question']))
    return 8


def eighth_response(bot, update, user_data):
    if update.message.text != test[7]['response']:
        update.message.reply_text(f'Неверно. Правильный ответ: {test[7]["response"]}')
    else:
        update.message.reply_text('Верно!')
        user_data['right_answers'] += 1

    update.message.reply_text(
        "{}".format(test[8]['question']))
    return 9


def ninth_response(bot, update, user_data):
    if update.message.text != test[8]['response']:
        update.message.reply_text(f'Неверно. Правильный ответ: {test[8]["response"]}')
    else:
        update.message.reply_text('Верно!')
        user_data['right_answers'] += 1

    update.message.reply_text(
        "{}".format(test[9]['question']))
    return 10


def tenth_response(bot, update, user_data):
    if update.message.text != test[9]['response']:
        update.message.reply_text(f'Неверно. Правильный ответ: {test[9]["response"]}')
    else:
        update.message.reply_text('Верно!')
        user_data['right_answers'] += 1
    print(user_data['right_answers'])
    update.message.reply_text(
        'Конец теста. Количество правильных ответов - {}/10'.format(user_data["right_answers"]))
    update.message.reply_text(
        'Желаете ли вы начать тест заново?'
    )
    return 11


def last_response(bot, update, user_data):
    print(123)
    if update.message.text.lower() == 'да':
        print(1)
        return 0

    print(0)
    update.message.reply_text('Ну ладно.')
    return ConversationHandler.END


def stop(bot, update):
    update.message.reply_text(
        "Ну ладно")
    return ConversationHandler.END


conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start,
                                 pass_user_data=True)],

    states={
        0: [MessageHandler(Filters.text, start,
                           pass_user_data=True)],
        1: [MessageHandler(Filters.text, first_response,
                           pass_user_data=True)],
        2: [MessageHandler(Filters.text, second_response,
                           pass_user_data=True)],
        3: [MessageHandler(Filters.text, third_response,
                           pass_user_data=True)],
        4: [MessageHandler(Filters.text, fourth_response,
                           pass_user_data=True)],
        5: [MessageHandler(Filters.text, fifth_response,
                           pass_user_data=True)],
        6: [MessageHandler(Filters.text, sixth_response,
                           pass_user_data=True)],
        7: [MessageHandler(Filters.text, seventh_response,
                           pass_user_data=True)],
        8: [MessageHandler(Filters.text, eighth_response,
                           pass_user_data=True)],
        9: [MessageHandler(Filters.text, ninth_response,
                           pass_user_data=True)],
        10: [MessageHandler(Filters.text, tenth_response,
                            pass_user_data=True)],
        11: [MessageHandler(Filters.text, last_response,
                            pass_user_data=True)]
    },

    fallbacks=[CommandHandler('stop', stop)]
)


def main():
    updater = Updater(input("Введите токен: "))

    dp = updater.dispatcher
    dp.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
