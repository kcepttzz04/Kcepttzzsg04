import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Thiết lập logging cơ bản để xem các thông báo từ bot
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Xử lý lệnh /start."""
    user = update.effective_user
    await update.message.reply_html(
        f"Xin chào {user.mention_html()}! Tôi là bot test của bạn.",
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo lại tin nhắn người dùng gửi."""
    await update.message.reply_text(update.message.text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Gửi tin nhắn trợ giúp khi lệnh /help được gọi."""
    await update.message.reply_text("Đây là bot test của bạn. Bạn có thể gõ bất cứ gì tôi sẽ lặp lại.")

def main() -> None:
    """Chạy bot."""
    # Lấy token từ biến môi trường
    BOT_TOKEN = os.environ.get('BOT_TOKEN')

    if not BOT_TOKEN:
        logger.error("BOT_TOKEN environment variable not set. Please set it on Railway.")
        exit(1) # Thoát nếu không có token

    # Tạo đối tượng Application và truyền token bot của bạn vào.
    application = Application.builder().token(BOT_TOKEN).build()

    # Thêm các trình xử lý lệnh và tin nhắn
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Bắt đầu bot
    logger.info("Bot đang bắt đầu polling...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()