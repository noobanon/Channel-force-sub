import os
from datetime import datetime

from pyrogram import filters
from pyrogram.types import User, InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.raw import functions
from pyrogram.errors import PeerIdInvalid
from pyrogram import Client
from Config import Config

@Client.on_message(filters.command("id", PREFIX) & filters.me)
async def id(client, message):
    cmd = message.command
    chat_id = message.chat.id
    if not message.reply_to_message and len(cmd) == 1:
        get_user = message.from_user.id
    elif len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
        try:
            get_user = int(cmd[1])
        except ValueError:
            pass
    try:
        user = await client.get_users(get_user)
    except PeerIdInvalid:
        await message.edit("I don't know that User.")
        return
    text = "**User ID**: `{}`\n**Chat ID**: `{}`".format(user.id, chat_id)
    await message.edit(text)
