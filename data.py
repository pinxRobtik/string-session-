from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton(" Mulai Ambil String ", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text=" Kembali ", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("Owner", url="https://t.me/cdkagenouu")],
        [
            InlineKeyboardButton("Bantuan", callback_data="help"),
            InlineKeyboardButton("Tentang Saya", callback_data="about")
        ],
        [InlineKeyboardButton("Support", url="https://t.me/cidsupport")],
    ]

    START = """
**Tentukan Pilihan** {}

**Selamat Datang Di** {}

**Ini Adalah Bot String Session

Buat Lu Maen Telegram**
    """

    HELP = """
**List Bantuan**

/about - Cek Nyet
/help - Cek Nyet
/start - Cek Nyet
/generate - Cek Nyet
/cancel - Cek Nyet
/restart - Cek Nyet
"""

    ABOUT = """
**Tentang Saya** 

**Saya Dibuat Oleh [cid](https://t.me/cdkagenouu)

Buat Lu Yang Maen Tele Ya..**

Gua Bukan ProDev Ya

Maintainer : @cidkagenouu**
    """
