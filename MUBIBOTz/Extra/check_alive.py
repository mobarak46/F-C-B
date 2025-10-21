# Basic health check command handler
async def alive(update, context):
    await update.message.reply_text("You're Lucky I'm alive and running!")
