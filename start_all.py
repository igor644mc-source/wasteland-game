import subprocess
import time

print("🚀 Запускаем локальный веб-сервер...")
# Было:
# server_process = subprocess.Popen(["python", "-m", "http.server", "8000"])

# Сделай вот так (добавь параметр --directory webapp):
server_process = subprocess.Popen(["python", "-m", "http.server", "8000", "--directory", "webapp"])

# Ждем секунду, чтобы сервер успел подняться
time.sleep(1)

print("🤖 Запускаем Telegram-бота...")
bot_process = subprocess.Popen(["python", "bot.py"])

try:
    # Держим процессы работающими
    server_process.wait()
    bot_process.wait()
except KeyboardInterrupt:
    print("\n🛑 Останавливаем все процессы...")
    server_process.terminate()
    bot_process.terminate()
