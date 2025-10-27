from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8444757889:AAF-ReV4kZg1gE4JHluAukA4NDTBN1bySAI"
WEBHOOK_URL = "https://telegram-bot2-juwu.onrender.com/webhook"

app = FastAPI()
bot_app = Application.builder().token(BOT_TOKEN).build()


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! ربات CTeamspeak فعاله ✅")


bot_app.add_handler(CommandHandler("start", start_handler))


@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, bot_app.bot)
    await bot_app.process_update(update)
    return {"ok": True}