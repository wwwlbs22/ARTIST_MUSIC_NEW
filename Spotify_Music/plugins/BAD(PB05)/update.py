import asyncio

from Spotify_Music import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import MUSIC_BOT_NAME

@app.on_message(filters.command(["repo"]))
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/c6e7be9e8ba1178fd82ef.mp4",
        caption=f"❤️ ʜᴇʏ {message.from_user.mention}",
        reply_markup=InlineKeyboardMarkup(
            [
               [
            InlineKeyboardButton(
                text="☆ ᴏᴡɴᴇʀ 💗 ", url=f"https://t.me/ARTIST_FEELINGS"
            ),
            InlineKeyboardButton(
                text="☆ ꜱᴜᴘᴘᴏʀᴛ 💗", url=f"https://t.me/Quiz2xf"
            ),
        ],
                [
                    InlineKeyboardButton(
                        "✯ ᴄʟᴏsᴇ ✯", callback_data="close"
                    )
                ],
            ]
        )
    )
  
# donate #
@app.on_message(filters.command(["donate, qr, scanner"]))
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/6473d213ad13d4803e37a.jpg",
        caption=f"❤️ ʜᴇʏ {message.from_user.mention}",
    )
