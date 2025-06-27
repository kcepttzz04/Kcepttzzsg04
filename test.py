from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get('BOT_TOKEN')

if not BOT_TOKEN:
    print("Error: BOT_TOKEN environment variable not set.")
    exit()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Đã nhận /start từ: {update.effective_user.id}")
    await update.message.reply_text("Chào bạn từ PTB 😄")

if __name__ == '__main__':
    app = ApplicationBuilder().token("BOT_TOKEN").build()

    app.add_handler(CommandHandler("start", start))

    print("Bot đang chạy nhé.")
    app.run_polling()
