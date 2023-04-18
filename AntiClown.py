# ---------------------------------------------------------------------------------
#  /\_/\
# ( o.o )  AntiClown модуль
#  > ^ <   Отправляет стикер в ответ на сообщение, если в сообщении найден смайл клоуна
# ---------------------------------------------------------------------------------
# Название: AntiClown
# Описание: Модуль для отправки стикера в ответ на сообщение, если в сообщении найден смайл клоуна
# Автор: your_username
# Команды: .anticlown, .anticlown on, .anticlown off
# Источник: https://github.com/your_username/AntiClown
# ---------------------------------------------------------------------------------

import random

from telethon.sync import TelegramClient
from telethon.events import NewMessage
from telethon.tl.types import PeerChannel

from .. import loader, utils


@loader.tds
class AntiClownMod(loader.Module):
    strings = {"name": "AntiClown"}

    def __init__(self):
        self.client = None
        self.enabled = True

    async def client_ready(self, client, db):
        self.client = client

    async def on_message(self, event):
        if self.enabled and event.sender_id != self.client.get_me().id:
            message = event.message.message
            if '🤡' in message:
                # Отправляем стикер в ответ на сообщение
                sticker_id = random.choice(['CAADAgAD6gIAAkcVaAnmSPU3MQq_jQI', 'CAADAgADyAMAAnbYEFKpBOCn1sFGHQI'])
                await self.client.send_file(event.chat_id, file=sticker_id, reply_to=event.id)

    async def anticlowncmd(self, m):
        """.anticlown - Включить/выключить AntiClown модуль"""
        self.enabled = not self.enabled
        if self.enabled:
            await self.client.send_message(m.chat_id, "AntiClown модуль включен!")
        else:
            await self.client.send_message(m.chat_id, "AntiClown модуль выключен!")

    async def anticlown_oncmd(self, m):
        """.anticlown on - Включить AntiClown модуль"""
        self.enabled = True
        await self.client.send_message(m.chat_id, "AntiClown модуль включен!")

    async def anticlown_offcmd(self, m):
        """.anticlown off - Выключить AntiClown модуль"""
        self.enabled = False
        await self.client.send_message(m.chat_id, "AntiClown модуль выключен!")
