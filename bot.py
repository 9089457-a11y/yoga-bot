import logging
import asyncio
import os
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Включаем логи
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

yoga_phrases = [
    "🌀 Инвентаризация чакр...",
    "🌊 Подключение к потоку...",
    "🎶 Громко пою Ом...",
    "🔥 Зажигаю внутренний огонь...",
    "🌸 Проверяю карму на свежесть...",
    "🧘 Настраиваю антенну на космос...",
    "💨 Дышу счастьем...",
    "🦋 Разворачиваю крылья души...",
    "🌞 Подзаряжаюсь от солнца...",
    "🌙 Настраиваюсь на лунный вайб...",
    "🥥 Открываю кокос внутренней гармонии...",
]

# пути к картинкам просто как имена файлов
yoga_asanas = [
    ("Натараджасана, поза короля танцев", "asana1.jpg"),
    ("Сварга Двиджасана, поза райской птицы", "asana2.jpg"),
    ("Бакасана", "asana3.jpg"),
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    phrases = random.sample(yoga_phrases, 3)

    message = await update.message.reply_text(phrases[0])
    for phrase in phrases[1:]:
        await asyncio.sleep(2)
        await message.edit_text(phrase)

    await asyncio.sleep(2)
    await message.delete()

    asana_name, asana_file = random.choice(yoga_asanas)

    # Отправляем картинку из корня проекта
    if os.path.exists(asana_file):
        with open(asana_file, "rb") as f:
            await update.message.reply_photo(photo=f, caption=asana_name)
    else:
        await update.message.reply_text(f"Файл {asana_file} не найден!")

def main() -> None:
    TOKEN = os.environ.get("TOKEN")
    PORT = int(os.environ.get("PORT", 5000))
    URL = "https://yoga-bot-lvzo.onrender.com"  # URL Render

    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))

    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=URL
    )

if __name__ == "__main__":
    main()
