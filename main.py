from os import *
from urllib.parse import *
from pyrogram.types import *
from pyrogram import *

pr0fess0r_99 = Client("ShareText-Bot",
    api_id=int(environ["API_ID"]), api_hash=environ["API_HASH"], bot_token=environ["BOT_TOKEN"])

@pr0fess0r_99.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    pr0fess0r99 = InlineKeyboardMarkup( [[ InlineKeyboardButton("My Channel", url="https://t.me/movie_supplier") ]] )
    await bot.send_photo(chat_id=update.chat.id, photo=environ.get("BOT_PIC", "https://telegra.ph/file/2b82d3a491f6b5869092c.jpg"),
        caption=f"__Hey {update.from_user.mention}__\n\n" + "__Iam A Telegram Text Message Sharing Link Creating Bot__" + "\n\n" + "__Maintained By [MoTech](t.me/mo_Tech_Group)__",
        reply_markup=pr0fess0r99, reply_to_message_id=update.id
    )

@pr0fess0r_99.on_message(filters.private & filters.text & ~filters.command(["start"]))
async def sharelink(bot, update):
    await bot.send_photo(chat_id=update.chat.id, photo=environ.get("BOT_PIC", "https://telegra.ph/file/2b82d3a491f6b5869092c.jpg"),
        caption=f"**Message Sharing Link Is Ready** :- https://t.me/share/url?url={quote(update.text)}", reply_to_message_id=update.id, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("📤 Share Link 📤", url=f"https://t.me/share/url?url={quote(update.text)}") ]] )       
    )

print("~~~~~~~~~~~")
print("Bot Started")
print("~~~~~~~~~~~")

pr0fess0r_99.run()
