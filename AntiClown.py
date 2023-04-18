# ---------------------------------------------------------------------------------
#  /\_/\
# ( -_- )  🌐 Этот модуль был загружен с GitHub: github.com
#  > 💀 <   🔐 Автор модуля: D4n13l3k00
# ---------------------------------------------------------------------------------
# Имя                                             : AntiClown
# Описание                                        : Модуль отправляет текст "те кто ставит реакцию клоуна тот террорист и фашист" при установке реакции "клоун" на сообщение
# Автор                                           : D4n13l3k00
# Команды                                         : .anticlown
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
        self.channel_id = None
        self.favorite_chat_id = None

    async def client_ready(self, client, db):
        self.client = client

    async def on_message(self, event):
        if self.favorite_chat_id is not None:
            if event.is_channel and event.message.to_id.channel_id == self.channel_id:
                if "🤡" in event.message.reactions:
                    # Отправляем сообщение при установке реакции "клоун"
                    await self.client.send_message(self.favorite_chat_id, "Те, кто ставит реакцию 'клоун', тот террорист и фашист!")

    async def anticlowncmd(self, m):
        """.anticlown - установить канал, для отслеживания установки реакции 'клоун' на сообщение"""
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
