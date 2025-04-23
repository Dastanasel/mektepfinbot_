import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 Сәлеметсіз бе! Бұл @MektepFinBot – мектеп қаржы менеджменті бойынша көмекші бот.\n\nТілді таңдаңыз:\n🇰🇿 /kaz – Қазақша\n🇷🇺 /rus – Русский")

async def kazakh(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Қазақ тілінде жұмыс басталды. Мәзір:\n/nuskau\n/kalkulyator\n/qurattar\n/kenes\n/keribailanys")

async def russian(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Вы выбрали русский язык. Меню:\n/instrukciya\n/kalkulyator\n/shablony\n/sovety\n/obratnayasvyaz")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("kaz", kazakh))
app.add_handler(CommandHandler("rus", russian))
app.run_polling()
