from pyrogram.types import Message
from pyrogram import Client, filters

from env import DATABASE_URL
from .basic import GUA
from bot import app
if DATABASE_URL != '':
    from Naya.database import SESSION
    from Naya.database.users_sql import Users, num_users, sempak


@Client.on_message(~filters.service, group=1)
async def users_sql(_, msg: Message):
    if DATABASE_URL == '':
        return
    if msg.from_user:
        q = SESSION.query(Users).get(int(msg.from_user.id))
        if not q:
            SESSION.add(Users(msg.from_user.id))
            SESSION.commit()
        else:
            SESSION.close()


@Client.on_message(filters.user(GUA) & filters.command("stats"))
async def _stats(_, msg: Message):
    if DATABASE_URL == '':
        return
    users = await num_users()
    await msg.reply(f"Total Users : {users}", quote=True)
    

@app.on_message(filters.user(GUA) & filters.command("apasih"))
async def gcast_handler(client, message):
    if len(message.command) > 1:
        text = ' '.join(message.command[1:])
    elif message.reply_to_message is not None:
        text = message.reply_to_message.text
    else:
        await message.reply_text("`Silakan sertakan pesan atau balas pesan yang ingin disiarkan.`")
        return
    if message.from_user.id not in GUA:
        await message.reply_text("Maaf, hanya ADMINS yang diizinkan menggunakan perintah ini.")
    babi = await lol()
    total_makhluk = 0
    for user in makhluk:
        try:
            await app.send_message(chat_id=user_id, text=text)
            total_babi += 1
        except:
            pass
    await message.reply_text(f"Pesan siaran berhasil dikirim kepada {total_makhluk} dari {len(makhluk)} pengguna.")