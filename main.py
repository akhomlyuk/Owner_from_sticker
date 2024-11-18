import asyncio
from pyrogram import Client
from pyrogram.raw.functions.messages import GetStickerSet
from pyrogram.raw.types.input_sticker_set_short_name import InputStickerSetShortName
import configparser as cfg

config = cfg.ConfigParser()
config.read('config.ini')

api_id = int(config.get("main", "api_id", fallback=0))
api_hash = config.get("main", "api_hash", fallback="")
bot_token = config.get("main", "bot_token", fallback="")
user_id = int(config.get("main", "user_id", fallback=0))

short_name = 'poxek'

async def main():
    async with Client("Exited3n", api_id=api_id, api_hash=api_hash, bot_token=bot_token) as app:
        sticker_set = InputStickerSetShortName(short_name=short_name)
        sticker_set = await app.invoke(GetStickerSet(stickerset=sticker_set, hash=0))

        set_id = sticker_set.set.id
        owner_id = sticker_set.set.id >> 32
        await app.send_message(user_id, f"<b>StickerSet ID</b>: <code>{set_id}</code>\n<b>Owner ID</b>: <code>{owner_id}</code>")


asyncio.run(main())
