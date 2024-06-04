from telethon import TelegramClient, events
import os

api_id = os.environ.get('API_ID')  # Ваш API ID
api_hash = os.environ.get('API_HASH')  # Ваш API HASH
session_name = 'telegram_client'

client = TelegramClient(session_name, api_id, api_hash)

# Обработчик новых сообщений
@client.on(events.NewMessage)
async def handler(event):
    try:
        print(event.message)
    except Exception as e:
        print(f"Ошибка при обработке сообщения: {e}")

# Основная функция
async def main():
    try:
        await client.start()
        print("Client Created")
        await client.run_until_disconnected()
    except Exception as e:
        print(f"Ошибка при запуске клиента: {e}")

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
