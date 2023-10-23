from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, _contexttypes
from typing import Final

TOKEN: Final = '6852536147:AAEMwVcCJRzqZPgTlnwB8rMblJteri-BnnY'
BOT_Username: Final = 'fwt_movierequesthandler_bot'

async def start_command(update: Update, context):
    await update.message.reply_text('Hey I am working, keep it up')

async def movie_req(update: Update, context):
    await update.message.reply_text('Your Movie Request has been taken. Please Wait. Admin Team will upload soon')

def handle_response(text: str) -> str:
    if 'hello' in text:
        return 'Hey, there'

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('movie', movie_req))

print('halal running')
app.run_polling(poll_interval=3)