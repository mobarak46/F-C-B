# Broadcast message to multiple users or groups
async def broadcast_message(users, message, context):
    for user_id in users:
        await context.bot.send_message(user_id, message)
