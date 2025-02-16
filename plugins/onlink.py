import os, asyncio
import time
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from plugins.authers import is_authorized
from Func.downloader import dl
from Func.utils import mention_user, generate_thumbnail, get_tg_filename

  

@Client.on_message(filters.regex(r'https?://[^\s]+'))
async def handle_link(client, message):
  link = message.text
  if "|" in link:
    link, newName = link.split("|")
  else:
    newName = None
    
  if not is_authorized(message.chat.id):
      await message.reply("**❌️You are not my auther for use me!...❌️**")
      return
  stT = f"🛠**Processing...**"
  msg = await message.reply(stT)
  dl_file = await dl(url=link, msg=msg, custom_filename=newName)
  if dl_file and not "error" in dl_file:
    
  else:
    return
  
  
