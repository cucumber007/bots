import json

from telegram.ext import Updater, CallbackQueryHandler, MessageHandler, Filters
from telegram.ext import CommandHandler


class Bot:

    last_messages = []

    def run(self):
        with open("../local-properties.json", "r") as f:
            token = json.loads(f.read())["anton"]
        updater = Updater(token=token)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("start", self.message))
        dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=self.message))

        # dispatcher.add_error_handler(self.handle_error)

        updater.start_polling()

    def message(self, bot, update, *kwargs):
        try:
            if len(self.last_messages) > 5:
                self.last_messages.pop(0)
            self.last_messages.append(update.message)
            if self.check_violation(self.last_messages):
                update.message.reply_text("Антон блять!")
        except Exception as e:
            update.message.reply_text("Ошибочка: " + str(e))

    def check_violation(self, messages):
        if len(messages) < 4:
            return False
        user = messages[0].from_user['id']
        for message in messages:
            if len(message.text) > 30:
                return False
            if message.from_user['id'] != user:
                return False
        return True


bot = Bot()
bot.run()

