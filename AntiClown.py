# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded from GitHub
# ( o.o )  🔐 Licensed under the CC BY-NC-ND 4.0.
#  > ^ <   ⚠️ Owner of romaterabyte doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name                                           : AntiClown
# Description                                    : A Telegram module that sends a specific sticker as a response to a clown reaction.
# Author                                         : romaterabyte
# Commands                                       :
# .setsticker | .setchat 
# ---------------------------------------------------------------------------------

from telethon.sync import TelegramClient
from telethon.events import NewMessage, ReactionUpdate
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon.tl.functions.messages import GetStickerSetRequest, GetEmojiKeywordsLanguageRequest, GetEmojiKeywordsRequest
from telethon.tl.functions.messages import GetEmojiKeywordsDifferenceRequest, SetEmojiKeywordsLanguageRequest
from telethon.tl.functions.messages import SetEmojiKeywordsRequest

from .. import loader, utils

@loader.tds
class AntiClownMod(loader.Module):
    strings = {"name": "AntiClown"}

    def __init__(self):
        self.client = None
        self.chat_id = None
        self.sticker_id = None

    async def client_ready(self, client, db):
        self.client = client

    async def on_message(self, event):
        pass

    async def on_reaction(self, event):
        if self.chat_id is not None and self.sticker_id is not None:
            if event.user_id != event.sender_id:
                return

            if event.is_reply and event.reply_to_msg_id and event.reply_to_msg_id == event.message_id:
                chat = await event.get_chat()
                if chat.id == self.chat_id and event.emoji == "🤡":
                    # Отправляем стикер при постановке реакции "🤡" на сообщение
                    await self.client.send_sticker(chat, self.sticker_id)

    async def setchatcmd(self, m):
        """.setchat <чат> - установить чат, в котором будет происходить отслеживание реакции клоуна"""
        args = utils.get_args_raw(m)
        if not args:
            await m.edit("<b>Укажите айди чата!</b>")
            return

        try:
            self.chat_id = int(args)
        except ValueError:
            await m.edit("<b>Неверный формат айди чата!</b>")
            return

        await m.edit(f"<b>Чат успешно установлен:</b> {args}")

    async def setstickercmd(self, m):
        """.setsticker <стикер> - установить стикер, который будет отправляться при постановке реакции клоуна"""
        args = utils.get_args_raw(m)
        if not args:
            await m.edit("<b>Укажите айди стикера!</b>")
            return

        try:
            self.sticker_id = args
        except ValueError:
            await m.edit("<b>Неверный формат айди стикера!</b>")
            return

        await m.edit(f"<b>Стикер успешно установлен:</b> {args}")
