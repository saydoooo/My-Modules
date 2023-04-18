# ---------------------------------------------------------------------------------
#  /\_/\
# ( o.o )  🔻 Модуль AntiClown
#  > ^ <   🔐 Лицензировано под CC BY-NC-ND 4.0
# ---------------------------------------------------------------------------------
# Название                                       : AntiClown
# Описание                                       : Этот модуль отправляет определенный стикер при постановке реакции "клоун" на сообщение
# Автор                                          : D4n13l3k00
# Команды                                        : .setsticker
# Загружено из                                   : github.com
# ---------------------------------------------------------------------------------

from telethon import events
from telethon.sync import TelegramClient

from .. import loader, utils


@loader.tds
class AntiClownMod(loader.Module):
    strings = {"name": "AntiClown"}

    def __init__(self):
        self.client = None
        self.sticker_id = None

    async def client_ready(self, client, db):
        self.client = client

    async def on_reaction(self, event):
        if self.sticker_id is not None and event.reaction == "🤡":
            await self.client.send_sticker(event.chat_id, self.sticker_id)

    async def setstickercmd(self, m):
        """.setsticker <стикер> - установить стикер, который будет отправляться при постановке реакции "клоун" на сообщение"""
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

