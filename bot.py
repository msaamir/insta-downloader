import os
import yt_dlp
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "8391666741:AAEojWSwIV3NpssPGMJZQJE49qHy1b-HNkQ"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    if "instagram.com" not in url:
        await update.message.reply_text("Bhai, Instagram link bhejo! 📥")
        return
    msg = await update.message.reply_text("Process ho raha hai... ⏳")
    try:
        ydl_opts = {'format': 'best', 'outtmpl': 'video.mp4', 'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        with open('video.mp4', 'rb') as video:
            await update.message.reply_video(video=video, caption="Done! ✅")
        os.remove('video.mp4')
        await msg.delete()
    except Exception as e:
        await msg.edit_text("Error! Link check karein.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
