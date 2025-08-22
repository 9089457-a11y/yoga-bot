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

# Прямые ссылки на картинки Google Drive
yoga_asanas = [
    ("Натараджасана, поза короля танцев", "https://drive.google.com/uc?export=view&id=1KCiUs9vsX_uz48LGCRFNe8brERwdOnRP"),
    ("Сварга Двиджасана, поза райской птицы", "https://drive.google.com/uc?export=view&id=1-_eJIXsPKOy_3eqEaDUgXBmkLzLL35dr"),
    ("Бакасана", "https://drive.google.com/uc?export=view&id=1k1GtWHC3bfMs44YG7CXVZ8qVKE8WuXrF"),
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
    asana_name, asana_url = random.choice(yoga_asanas)

    # Отправляем картинку с асаной по URL
    await update.message.reply_photo(photo=asana_url, caption=asana_name)


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
