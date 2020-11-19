import json
import random

from telegram.ext import Updater, CallbackQueryHandler, MessageHandler, Filters
from telegram.ext import CommandHandler


class Bot:

    counter = 0

    zavali = [
        "Закрой ебало",
        "Забей ебало",
        "Стяни ебало",
        "Закрой ебальник",
        "Закрой пиздачело",
    ]

    def run(self):
        with open("local-properties.json", "r") as f:
            token = json.loads(f.read())["token"]
        updater = Updater(token=token, use_context=True)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("start", self.message))
        dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=self.message))

        # dispatcher.add_error_handler(self.handle_error)

        updater.start_polling()

    def message(self, update, context):
        try:
            username = update.message.from_user['username']
            text = update.message.text
            if "ymlnv" in username or "--test" in text:
                if self.counter < 25:
                    self.counter += 1
                else:
                    self.counter = 0
                    reply = self.zavali[random.randint(0, len(self.zavali) - 1)]
                    update.message.reply_text(reply)

                # ran = random.random()
                # if ran < 0.5:
                #     reply = "Завали ебало!"
                # else:
                #     if ran < 0.9:
                #         reply = self.zavali[random.randint(0, len(self.zavali)-1)]
                #     else:
                #         reply = "Пидор!"
                # update.message.reply_text(reply)

        except Exception as e:
            update.message.reply_text("Ошибочка: " + str(e))



bot = Bot()
bot.run()


