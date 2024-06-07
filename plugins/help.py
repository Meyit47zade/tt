from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Sahip Olduklarım", url="https://t.me/OfficialKiyiciSahip")
      ],
      [ 
        InlineKeyboardButton(
            "Support", url="https://t.me/officiallKiyici")]
    ])  
    helptxt = f"<b> Video veya ses formatında indirmek için bir Youtube URL'si göndermeniz yeterli!\n\n - @Meyitzade </b>"
    await message.reply_text(helptxt, reply_markup=joinButton)
