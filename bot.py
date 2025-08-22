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

yoga_asanas = [
    ("Натараджасана, поза короля танцев", "images/asana1.jpg"),
    ("Сварга Двиджасана, поза райской птицы", "images/asana2.jpg"),
    ("Бакасана", "images/asana3.jpg"),
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Берем 3 случайные фразы без повторений
    phrases = random.sample(yoga_phrases, 3)

    message = await update.message.reply_text(phrases[0])
    for phrase in phrases[1:]:
        await asyncio.sleep(2)
        await message.edit_text(phrase)

    # После показа фраз удаляем сообщение
    await asyncio.sleep(2)
    await message.delete()

    # Выбираем случайную асану
    asana_name, asana_file = random.choice(yoga_asanas)

    # Отправляем картинку с асаной
    with open(asana_file, "rb") as f:
        await update.message.reply_photo(photo=f, caption=asana_name)


def main() -> None:
    TOKEN = os.environ.get("TOKEN")
    PORT = int(os.environ.get("PORT", 5000))
    URL = "https://yoga-bot-lvzo.onrender.com"  # публичный URL Render

    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))

    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=URL
    )

if __name__ == "__main__":
    main()
