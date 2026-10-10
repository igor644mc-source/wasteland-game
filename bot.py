# bot.py
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

from database import init_db, get_player

# Вставь сюда токен своего бота, который тебе выдал @BotFather
TOKEN = "8943023278:AAFpje18w1K3R1GCmVC2x7REEgSQe5h2IGw"

# Включаем логирование
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    # Инициализируем/проверяем игрока в базе
    player = get_player(user_id)
    
    # Создаем клавиатуру с кнопкой открытия Mini App
    # ВАЖНО: Вместо 'https://t.yourdomain.com' потом нужно будет указать ссылку на твой запущенный сайт/веб-приложение
    webapp_url = webapp_url = "https://brownnose-survive-crimson.ngrok-free.dev" 
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="☢️ Войти в Пустошь", 
                    web_app=WebAppInfo(url=webapp_url)
                )
            ]
        ]
    )
    
    await message.answer(
        f"Привет, выживший! 🌲\n"
        f"Твои текущие показатели:\n"
        f"❤️ Здоровье: {player['hp']}\n"
        f"💧 Вода: {player['water']}\n"
        f"🎒 Лут: {player['loot']}\n\n"
        f"Нажми кнопку ниже, чтобы открыть интерфейс игры:",
        reply_markup=keyboard
    )

async def main():
    # Инициализируем базу данных при старте
    init_db()
    print("Бот запущен и готов к работе...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())