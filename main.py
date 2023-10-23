from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, _contexttypes
from typing import Final

TOKEN: Final = '6709054620:AAHDKRMBsT6lfwUV4GvmnRWidujIBVLZWss'
BOT_Username: Final = '@diamonduser_bot'

async def start_command(update: Update, context):
    await update.message.reply_text('Hey I am working, keep it up')

async def help(update: Update, context):
    await update.message.reply_text('admin will contract you')

def handle_response(text: str) -> str:
    if 'hello' in text:
        return 'Hey, there'

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help', help))

print('running')
app.run_polling(poll_interval=3)
