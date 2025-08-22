import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random
import os

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
    # Отправляем первое сообщение
    message = await update.message.reply_text(yoga_phrases[0])

    # Меняем текст несколько раз с паузами
    for phrase in yoga_phrases[1:]:
        await asyncio.sleep(2)  # задержка 2 сек
        await message.edit_text(phrase)

    # Ждём и удаляем сообщение
    await asyncio.sleep(2)
    await message.delete()

    # Выбираем случайную асану
    asana_name, asana_file = random.choice(yoga_asanas)

    # Отправляем картинку + название асаны
    with open(asana_file, "rb") as f:
        await update.message.reply_photo(photo=f, caption=asana_name)

def main() -> None:
    # 🔑 сюда вставь свой токен
    TOKEN = os.environ.get("TOKEN")

    # Создаем приложение
    application = Application.builder().token(TOKEN).build()

    # Регистрируем команду /start
    application.add_handler(CommandHandler("start", start))

    # Запуск бота
    application.run_polling()

if __name__ == "__main__":
    main()
