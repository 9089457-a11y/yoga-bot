import logging
import asyncio
import os
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Включаем логи для отладки
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Список фраз
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

# Список асан (название + файл картинки/гиф)
yoga_asanas = [
    ("Натараджасана, поза короля танцев", "images/asana1.jpg"),
    ("Сварга Двиджасана, поза райской птицы", "images/asana2.jpg"),
    ("Бакасана", "images/asana3.jpg"),
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = await update.message.reply_text(yoga_phrases[0])
    for phrase in yoga_phrases[1:]:
        await asyncio.sleep(2)
        await message.edit_text(phrase)
    await asyncio.sleep(2)
    await message.delete()
    asana_name, asana_file = random.choice(yoga_asanas)
    with open(asana_file, "rb") as f:
        await update.message.reply_photo(photo=f, caption=asana_name)

def main() -> None:
    TOKEN = os.environ.get("TOKEN")
    URL = os.environ.get("RENDER_EXTERNAL_URL")  # Render автоматически задаёт внешний URL
    PORT = int(os.environ.get("PORT", 5000))

    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))

    # Запуск через webhook
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=f"{URL}/webhook/{TOKEN}"
    )

if __name__ == "__main__":
    main()
