# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded from github.com
# ( o.o )  🔐 Licensed under the CC BY-NC-ND 4.0.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name                                           : NewPostsNotifier
# Description                                    : Модуль для уведомления о новых постах в канале
# Author                                         : romaterabyte
# Commands                                       :
# .setchannel | .setfavorite
# ---------------------------------------------------------------------------------

import random

from telethon.sync import TelegramClient
from telethon.events import NewMessage
from telethon.tl.types import PeerChannel

from .. import loader, utils


@loader.tds
class NewPostsNotifierMod(loader.Module):
    strings = {"name": "Уведомитель о новых постах"}

    def __init__(self):
        self.client = None
        self.channel_id = None
        self.favorite_chat_id = None

    async def client_ready(self, client, db):
        self.client = client

    async def on_message(self, event):
        if self.favorite_chat_id is not None:
            if event.is_channel and event.message.to_id.channel_id == self.channel_id:
                if event.message.post:
                    # Отправляем уведомление о новом посте в избранное
                    await self.client.send_message(self.favorite_chat_id, "Новый пост в канале!")

    async def setchannelcmd(self, m):
        """.setchannel <канал> - установить канал, для которого будет производиться отслеживание новых постов"""
        args = utils.get_args_raw(m)
        if not args:
            await m.edit("<b>Укажите айди канала!</b>")
            return

        try:
            self.channel_id = int(args)
        except ValueError:
            await m.edit("<b>Неверный формат айди канала!</b>")
            return

        await m.edit(f"<b>Канал успешно установлен:</b> {args}")

    async def setfavoritecmd(self, m):
        """.setfavorite <чат> - установить чат, в который будет отправляться уведомление о новых постах"""
        args = utils.get_args_raw(m)
        if not args:
            await m.edit("<b>Укажите айди чата избранного!</b>")
            return

        try:
            self.favorite_chat_id = int(args)
        except ValueError:
            await m.edit("<b>Неверный формат айди чата избранного!</b>")
            return

        await m.edit(f"<b>Чат избранного успешно установлен:</b> {args}")
