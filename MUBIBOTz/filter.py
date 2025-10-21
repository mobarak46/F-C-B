# Placeholders for custom filters (e.g. filter messages/users)
def is_valid_file(update):
    return bool(update.message.document or update.message.photo)
