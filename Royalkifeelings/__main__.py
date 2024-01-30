import asyncio
import importlib
from pytgcalls import idle
from K_King_HYT.callmusic.config import BOT_USERNAME
from K_King_HYT import bot, call_py
from K_King_HYT.plugins import ALL_PLUGINS


loop = asyncio.get_event_loop()


async def K_King_HYT():
    for all_module in ALL_PLUGINS:
        importlib.import_module("K_King_HYT.plugins." + all_module)
    await bot.start()
    await call_py.start()
    await idle()
    print(f"ɢᴏᴏᴅʙʏᴇ!\nStopping @{BOT_USERNAME}")
    await bot.stop()


if __name__ == "__main__":
    loop.run_until_complete(K_King_HYT())
