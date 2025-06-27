import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Thiết lập logging cơ bản
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Xử lý lệnh /start."""
    user = update.effective_user
    await update.message.reply_html(
        f"Xin chào {user.mention_html()}! Tôi là Trợ Lý của bạn.",
    )
    await task(update, context)  # Đừng quên await

async def task(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Xử lý hiển thị menu task."""
    keyboard = [
        [InlineKeyboardButton("Thêm công việc", callback_data='add_task')],
        [InlineKeyboardButton("Xem công việc", callback_data='view_task')],
        [InlineKeyboardButton("Hoàn thành công việc", callback_data='end_task')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text('Chọn một lựa chọn:', reply_markup=reply_markup)
    elif update.callback_query:
        query = update.callback_query
        await query.message.edit_text('Chọn một lựa chọn:', reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Đây là bot test của bạn. Gõ /start để hiển thị menu task.")

def main() -> None:
    BOT_TOKEN = os.environ.get('BOT_TOKEN')

    if not BOT_TOKEN:
        logger.error("BOT_TOKEN environment variable not set. Please set it on Railway.")
        exit(1)

    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    logger.info("Bot đang bắt đầu polling...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
