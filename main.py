import telebot
from telebot import types
from telebot.types import (
    ForceReply,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove
)
from datetime import datetime
import json
import re
import logging
import requests  # Thêm requests để gửi feedback
#API_KEY
API_KEY = "7834084785:AAHt36k1GDCq7GzbUMfzxz2UrGUaMD32v60"
bot = telebot.TeleBot(API_KEY)
# Thời gian hiện tại
def thoi_gian_hien_tai():
    return datetime.now().strftime('%H:%M:%S ngày %d/%m/%Y')
# Cấu hình logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)