from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Đã nhận /start từ: {update.effective_user.id}")
    await update.message.reply_text("Chào bạn từ PTB 😄")

if __name__ == '__main__':
    app = ApplicationBuilder().token("8099339703:AAHINPHp70N9r0VOXCIa1fQshcYWRZONWf8").build()

    app.add_handler(CommandHandler("start", start))

    print("Bot đang chạy...")
    app.run_polling()
