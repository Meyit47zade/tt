
from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Sahip Olduklarım", url="https://t.me/OfficiallKiyiciSahip")
      ],
      [ 
        InlineKeyboardButton(
            "Support", url="https://t.me/OfficialKiyici")]
    ])
    welcomed = f"<b> Merhaba {message.from_user.first_name}, \n\nBen YouTube DL Bot'um. Youtube'dan video veya ses indirebilirim. \n\nDaha fazla bilgi için /help - @OfficialKiyici </b>"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagatio
