from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("⚙ بدء استخراج جلسه البوت ⚙", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="عوده الى القائمه الرئيسيه", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("👨‍💻 المطور 👨‍💻", url="https://t.me/N_B_1")],
        [
            InlineKeyboardButton("❔ How to Use ❔", callback_data="help"),
            InlineKeyboardButton("ℹ About ℹ", callback_data="about")
        ],
    ]

    START = """
Hey {}

مرحبا في {}

استخدم هذا الروبوت فقط إذا كنت تثق في هذا البوت ، اذا كنت لا تثق بهذا البوت فقم بحذف هذه الدردشة ولا تستخدمها.

أنا جلسة سلسلة مولد بوت ل Pyrogram & Telethon.

انقر على الأزرار أدناه لمعرفة المزيد. 
    """

    HELP = """
🔥 *الاوامر الشغاله** 🔥

`/about` - عن البوت بشكل تفصيلي.
`/help` - لاضهار هذه الرساله.
`/start` - للبدء.
`/generate` - لاستخراج جلسه البوت.
`/cancel` - لالغاء الجلسه.
`/restart` - لاعاده تشغيل البوت.
"""

    ABOUT = """
🔥 **شرح عن هذا البوت** 🔥

**Telegram Bot to generate Pyrogram and Telethon string session.**

**Framework** : [Pyrogram](https://docs.pyrogram.org)

**Language** : [Python](https://www.python.org)
    """
