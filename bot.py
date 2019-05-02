from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler
from random import shuffle
import json

with open("test.json", "rt", encoding="utf8") as f:
    test = json.loads(f.read())['test']


def start(bot, update):
    shuffle(test)
    update.message.reply_text(
        "Привет. Это тест по истории, состоящий из 6 перемешанных вопросов\n"
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
    print(user_data['right_answers'])
    update.message.reply_text(
        'Конец теста. Количество правильных ответов - {}/6'.format(user_data["right_answers"]))
    return ConversationHandler.END


def stop(bot, update):
    update.message.reply_text(
        "Ну ладно")
    return ConversationHandler.END


conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],

    states={
        # Добавили user_data для сохранения ответа.
        1: [MessageHandler(Filters.text, first_response,
                           pass_user_data=True)],
        # ...и для его использования.
        2: [MessageHandler(Filters.text, second_response,
                           pass_user_data=True)],
        3: [MessageHandler(Filters.text, third_response,
                           pass_user_data=True)],
        4: [MessageHandler(Filters.text, fourth_response,
                           pass_user_data=True)],
        5: [MessageHandler(Filters.text, fifth_response,
                           pass_user_data=True)],
        6: [MessageHandler(Filters.text, sixth_response,
                           pass_user_data=True)]
    },

    fallbacks=[CommandHandler('stop', stop)]
)


def main():
    updater = Updater("845010139:AAEtih9AAKtMBVRc0kvrmVAeQ712l9EYyhg")

    dp = updater.dispatcher
    dp.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
