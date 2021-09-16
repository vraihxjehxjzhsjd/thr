import threading, pyrogram, asyncio
from pyrogram import filters
global count
count = 0

def start_client(app):
    with app:
        me = app.get_me()
        print(f"Log as @{me.username}")
    @app.on_message(filters.command("а", "а"))
    async def flood(client, message):
        try:
            a = count
            del a
        except:
            count = 0
        while True:
            count += 1
            try:
                await client.send_message(message.chat.id, f"test {count}")
            except:
                pass
            print(f"sended. COUNT: {count}")
    app.run()

clients = [pyrogram.Client("1", bot_token="1951351434:AAF6robWwzaRZ7FMmBEE9NEW22IQOEUXGcw"), pyrogram.Client("2", bot_token="1920365445:AAGLxcah_iX2GePwSvxo-sc8VX2ZRrxiwSI")]
for client in clients:
    threading.Thread(start_client(app=client)).start()
    print(f"send 'ок' to chat")
    pyrogram.idle()
            
