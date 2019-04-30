# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from datetime import datetime
import json

with open("test.json", "rt", encoding="utf8") as f:
    test = json.loads(f.read())['test']
print(test)

# Напишем соответствующие функции.
# Их сигнатура и поведение аналогичны обработчикам текстовых сообщений.
def start(bot, update):
    updater = Updater("845010139:AAEtih9AAKtMBVRc0kvrmVAeQ712l9EYyhg")
    test.reverse()
    update.message.reply_text(
        "Привет! Сейчас будет тест по истории!"
    )
    updater.start_polling()
    update.message.reply_text("Привет")



def help(bot, update):
    update.message.reply_text(
        "Я пока не умею помогать... Я только ваше эхо.")


def time(bot, update):
    update.message.reply_text(datetime.strftime(datetime.now(), "%H:%M:%S"))


def date(bot, update):
    update.message.reply_text(datetime.strftime(datetime.now(), "%x"))


# Определяем функцию-обработчик сообщений.
# У неё два параметра, сам бот и класс updater, принявший сообщение.
def echo(bot, update):
    # У объекта класса Updater есть поле message, являющееся
    # объектом сообщения.
    # У message есть поле text, содержащее текст полученного сообщения,
    # а также метод reply_text(str), отсылающий ответ пользователю,
    # от которого получено сообщение.
    text = list(update.message.text)
    text.reverse()
    update.message.reply_text(''.join(text))


def main():
    # Создаём объект updater. Вместо слова "TOKEN" надо разместить
    # полученный от @BotFather токен
    updater = Updater("845010139:AAEtih9AAKtMBVRc0kvrmVAeQ712l9EYyhg")

    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher

    # Зарегистрируем их в диспетчере рядом с регистрацией
    # обработчиков текстовых сообщений.
    # Первым параметром конструктора CommandHandler является название команды.
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("time", time))
    dp.add_handler(CommandHandler("date", date))

    # Создаём обработчик сообщений типа Filters.text
    # из описанной выше функции echo()
    # После регистрации обработчика в диспетчере эта функция
    # будет вызываться при получении сообщения с типом "текст",
    # т.е. текстовых сообщений.
    text_handler = MessageHandler(Filters.text, echo)

    # Регистрируем обработчик в диспетчере.
    dp.add_handler(text_handler)

    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()

    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
