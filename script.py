import os
import info from script
import img2pdf

def image_to_pdf(input_path, output_path):
    with open(output_path, "wb") as f:
        f.write(img2pdf.convert(input_path))
    return output_path
class script(object):

    START_TXT = """<b>ʜɪɪ {}, 

ɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀꜰᴜʟ ʙᴏᴛ.

ʏᴏᴜ ᴄᴀɴ ᴘᴍ



<b><blockquote>🌿 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href="https://t.me/Mobarak46">Mubi</a></b></b></blockquote>"""

    

    HELP_TXT = """<b>ʜᴇʟʟᴏ {}

ʜᴇʀᴇ ɪs ᴀʟʟ ᴍʏ ᴜsᴇғᴜʟʟ ғᴇᴀᴛᴜʀᴇs.</b></b>"""



    ABOUT_TXT = """<b>✯ ᴍʏ ɴᴀᴍᴇ : <a href=https://t.me/{}>{}</a>

✯ ᴄʀᴇᴀᴛᴏʀ : <a href=https://t.me/{}>Mubi</a>

✯ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a>

✯ ʟᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/download/releases/3.0/'>ᴘʏᴛʜᴏɴ 𝟹</a> 

✯ ᴅᴀᴛᴀʙᴀꜱᴇ : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a> 

✯ ʜᴏꜱᴛᴇᴅ ᴏɴ : <a href='https://www.render.com/'>ʀᴇɴᴅᴇʀ</a>

✯ ʙᴜɪʟᴅ ꜱᴛᴀᴛᴜꜱ : v4.54.9 </b></b>"""

    
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

    ADMIN_TXT = """<b><blockquote>ʜᴇʟᴘ: Aᴅᴍɪɴ Mᴏᴅs

<b>ɴᴏᴛᴇ:</b>

Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs

Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:

• /logs - <code>ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ</code>

• /stats - <code>ᴛᴏ ɢᴇᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ᴅʙ. [Tʜɪs Cᴏᴍᴍᴀɴᴅ Cᴀɴ Bᴇ Usᴇᴅ Bʏ Aɴʏᴏɴᴇ]</code>

• /delete - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ .</code>


• /ban  - <code>ᴛᴏ ʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>

• /unban  - <code>ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>

• /broadcast - <code>ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ</code></b></blockquote>"""



    MUBI_STATUS_TXT = """<b><blockquote><u>🌀 Mᴏɴɢᴏ Dᴀʀᴀʙᴀsᴇ </u>


👤 Tᴏᴛᴀʟ Usᴇʀs : <code>{}</code>

💌 Usᴇᴅ Sᴛᴏʀᴀɢᴇ : <code>{} Mb</code>

🎉 Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ : <code>{} Mb</code> </b></blockquote>"""



    DEL_LNK_TXT = """<b><blockquote> <u>🚫 Dᴇʟᴇᴛᴇᴅ Lɪɴᴋ Mᴇssᴀɢᴇ ⚙️</u>

👤Usᴇʀ Nᴀᴍᴇ : {}

🪪Usᴇʀ Iᴅ : {}

📚Usᴇʀ Cʜᴀᴛ : {}

📝Usᴇʀ Cʜᴀᴛ Iᴅ: {}

🗃️Usᴇʀ Mᴇssᴀɢᴇ : {}

📢Fʀᴏᴍ Bᴏᴛ Nᴀᴍᴇ Is Rᴇᴘᴏʀᴛᴇᴅ : <a href=https://t.me/{}>{}</a></b></blockquote>"""



    REQALART_LNK_TXT = """<b><blockquote><u>💻 Tʀɪɢɢᴇʀᴇᴅ🎭</u>

👤Usᴇʀ Nᴀᴍᴇ : {}

🪪Usᴇʀ Iᴅ : {}

📚Usᴇʀ Cʜᴀᴛ : {}

📝Usᴇʀ Cʜᴀᴛ Iᴅ: {}

🗃️Usᴇʀ Mᴇssᴀɢᴇ : {}

📢Fʀᴏᴍ Bᴏᴛ Nᴀᴍᴇ Is Rᴇᴘᴏʀᴛᴇᴅ : <a href=https://t.me/{}>{}</a></b></blockquote>"""

    

    LOG_TEXT_G = """<b><blockquote> #NewGroup

Gʀᴏᴜᴘ = {}(<code>{}</code>)

Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs = <code>{}</code>

Aᴅᴅᴇᴅ Bʏ - {}

Bᴏᴛ @yourbotusername </b></blockquote>"""



    LOG_TEXT_P = """<b><blockquote> #NewUser

ID - <code>{}</code>

Nᴀᴍᴇ - {}

Bᴏᴛ @yourbotusername </b></blockquote>"""



    MUBI_FILE_CAPTION = """<b>{file_name}</b>""" 



    LOG_TXT = """<b><blockquote>

📀 Bot run time: {runtime} Minutes

📆 task completed in: {remaining_seconds} <i>seconds</i> 🔥



Requested by : {message.from_user.mention}</b> </b></blockquote>"""

    

    PROGRESS_BAR = """\n<b><blockquote>

╭━━━━❰ ғɪʟᴇ ɪs ʀᴇɴᴀᴍɪɴɢ... ❱━➣

┣⪼ 🗂️ : {1} | {2}

┣⪼ ⏳️ : {0}%

┣⪼ 🚀 : {3}/s

┣⪼ ⏱️ : {4}

╰━━━━━━━━━━━━━━━➣ </b></blockquote>"""

 

    RESTART_TXT = """<b><blockquote>𝐁ᴏᴛ 𝐑ᴇsᴛᴀʀᴛᴇᴅ !

📅 𝐃ᴀᴛᴇ : <code>{}</code>

⏰ 𝐓ɪᴍᴇ : <code>{}</code>

🌐 𝐓ɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>

🛠️ 𝐁ᴜɪʟᴅ 𝐒ᴛᴀᴛᴜs: <code>ᴠ7.𝟶 [ Sᴛᴀʙʟᴇ </code>

💌 𝐁ᴏᴛ 𝐍ᴀᴍᴇ:-<a href=https://t.me/{}>{}</a> </b></blockquote>"""



    LOGO = """BOT IS SUCCESSFULLY DEPLOYED AND WORKING"""
