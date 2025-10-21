import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from info import DESCRIPTION, AUTHOR, VERSION
from script import image_to_pdf
from config import BOT_TOKEN

async def start(update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"{DESCRIPTION} by {AUTHOR}
Version: {VERSION}
Send me images to convert to PDF!")

async def handle_image(update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.photo[-1].get_file()
    input_path = f"downloads/{file.file_id}.jpg"
    output_path = f"downloads/{file.file_id}.pdf"
    await file.download_to_drive(input_path)
    pdf_path = image_to_pdf(input_path, output_path)
    await update.message.reply_document(pdf_path)

def main():
    if not os.path.exists("downloads"):
        os.makedirs("downloads")
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_image))
    app.run_polling()

if __name__ == "__main__":
    main()
