from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("باز کردن لینک", url="https://example.com")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("خوش آمدید! روی دکمه زیر کلیک کنید:", reply_markup=reply_markup)

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
