from os import environ
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

crown_botz=Client(
    "ᴀᴜᴛᴏ ᴀᴘᴘʀᴏᴠᴇᴅ ʙᴏᴛ",
    bot_token = environ["BOT_TOKEN"],
    api_id = int(environ["API_ID"]),
    api_hash = environ["API_HASH"]
)

CHAT_ID = [int(crown_botz) for crown_botz in environ.get("CHAT_ID", None).split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "ʜᴇʟʟᴏ {mention}\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {title}\n\nʏᴏᴜʀ ᴀᴜᴛᴏ ᴀᴘᴘʀᴏᴠᴇᴅ ʙʏ ᴍᴇ")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

@crown_botz.on_message(filters.private & filters.command(["start"]))
async def start(client: crown_botz, message: Message):
    approvedbot = await client.get_me() 
    button = [[ InlineKeyboardButton("ʀᴇᴘᴏ", url="https://github.com/dor3Monbotz/DoraAutoApproveBot"), InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ 📢", url="https://t.me/+OUZXn9nigZYxOWU9") ],
              [ InlineKeyboardButton("➕️ ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ➕️", url=f"http://t.me/{approvedbot.username}?startgroup=botstart") ]]
    await client.send_message(chat_id=message.chat.id, text=f"**__ʜᴇʟʟᴏ {message.from_user.mention} ɪᴀᴍ ᴀᴜᴛᴏ ᴀᴘᴘʀᴏᴠᴇʀ ᴊᴏɪɴ ʀᴇǫᴜᴇsᴛ ʙᴏᴛ ᴊᴜsᴛ [ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ](http://t.me/{approvedbot.username}?startgroup=botstart) || Repo Sorry But Repo is now private some reasons||**__", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@crown_botz.on_chat_join_request((filters.group | filters.channel) & filters.chat(CHAT_ID) if CHAT_ID else (filters.group | filters.channel))
async def autoapprove(client: crown_botz, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} 🤝ᴛʜᴀɴᴋs ғᴏʀ ᴊᴏɪɴɪɴɢ🤝") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title))
    #   print("Welcome....")

print("Crown Auto Approved Bot")
crown_botz.run()
