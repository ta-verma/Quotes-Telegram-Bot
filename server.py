from telegram.ext import Updater, CommandHandler
import logging, os
import qoutes as qt

PORT = int(os.environ.get('PORT', 5000))

TOKEN = 'Place TOKEN Here'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome, send /next to get a quote!")

def bothelp(update, context):
    update.message.reply_text("send /next to get a quote")

def getQuote(update, context):
    update.message.reply_text(qt.text())
    
def feedback(update, context):
	update.message.reply_text("send your feedback/request to @monstersupportbot\n\nNote: Please mention the Bot name in your feedback")

def main():
	updater = Updater(TOKEN, use_context=True)

	updater.dispatcher.add_handler(CommandHandler('start', start))
	updater.dispatcher.add_handler(CommandHandler('help', bothelp))
	updater.dispatcher.add_handler(CommandHandler('feedback', feedback))
	updater.dispatcher.add_handler(CommandHandler('next', getQuote))
	updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN)
	updater.bot.setWebhook('https://quotes101.herokuapp.com/' + TOKEN)
	updater.idle()


if __name__ == '__main__':
    main()
