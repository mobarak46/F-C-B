from telegram.ext import CommandHandler

def get_handlers():
    return [
        CommandHandler("start", start_command),
        # Add more command handlers here
    ]

async def start_command(update, context):
    await update.message.reply_text("Welcome to the Mubi File Converter Bot\n\n Send me the file and convert into as you wish\n\n You can Send files 1MB to 4GB\n\n Maintained by @Mobarak46")
