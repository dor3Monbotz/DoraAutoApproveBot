from os import environ
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

ap= 19099900
hs="2b445de78e5baf012a0793e60bd4fbf5"
bt="5905912080:AAH1PraNYThzXvG8OOGbECo2DSdaUfFD88g"

kunal=Client("Auto Approved Bot",bot_token=bt ,api_id=ap ,api_hash=hs)

CHAT_ID= 1572592335
TEXT="ʜᴇʟʟᴏ {mention}\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {title}\n\nʏᴏᴜ ɢᴇᴛ ᴀᴜᴛᴏ ᴀᴘᴘʀᴏᴠᴇᴅ ʙʏ ᴍᴇ\n ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ @LMbackups "
APPROVED="on"

@kunal.on_message(filters.private & filters.command(["start"]))
async def start(client: kunal, message: Message):
    approvedbot = await client.get_me() 
    button = [[ InlineKeyboardButton("ʀᴇᴘᴏ", url="https://github.com/dor3Monbotz/DoraAutoApproveBot"), InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ 📢", url="https://t.me/+OUZXn9nigZYxOWU9") ],
              [ InlineKeyboardButton("➕️ ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ➕️", url=f"http://t.me/{approvedbot.username}?startgroup=botstart") ]]
    await client.send_message(chat_id=message.chat.id, text=f"**__ʜᴇʟʟᴏ {message.from_user.mention} ɪᴀᴍ ᴀᴜᴛᴏ ᴀᴘᴘʀᴏᴠᴇʀ ᴊᴏɪɴ ʀᴇǫᴜᴇsᴛ ʙᴏᴛ ᴊᴜsᴛ [ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ](http://t.me/{approvedbot.username}?startgroup=botstart) || Repo Sorry But Repo is now private some reasons||**__", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@kunal.on_chat_join_request((filters.group | filters.channel) & filters.chat(CHAT_ID) if CHAT_ID else (filters.group | filters.channel))
async def autoapprove(client: kunal, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} 🤝ᴛʜᴀɴᴋs ғᴏʀ ᴊᴏɪɴɪɴɢ🤝") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title))
    #   print("Welcome....")

print("Auto Approved Bot")
kunal.run()
