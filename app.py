import os
from flask import Flask, request, jsonify
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from wildberries_parser import get_wildberries_items

# Получаем API ID и API HASH из переменных окружения
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
session_name = 'session_name'

# Проверяем, что API ID и API HASH заданы
if not api_id or not api_hash:
    raise ValueError("API_ID and API_HASH must be set")

# Создаем экземпляр TelegramClient
client = TelegramClient(session_name, api_id, api_hash)

# Создаем экземпляр Flask
app = Flask(__name__)


@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    user_id = data.get('user_id')
    message = data.get('message')

    if not user_id or not message:
        return jsonify({'error': 'user_id and message are required'}), 400

    with client:
        client.loop.run_until_complete(client.send_message(user_id, message))

    return jsonify({'status': 'message sent'})


@app.route('/send_media', methods=['POST'])
def send_media():
    data = request.json
    user_id = data.get('user_id')
    media_path = data.get('media_path')

    if not user_id or not media_path:
        return jsonify({'error': 'user_id and media_path are required'}), 400

    with client:
        client.loop.run_until_complete(client.send_file(user_id, media_path))

    return jsonify({'status': 'media sent'})


@app.route('/login_qr', methods=['GET'])
def login_qr():
    with client:
        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone)
            try:
                client.sign_in(phone, input('Enter the code: '))
            except SessionPasswordNeededError:
                client.sign_in(password=input('Password: '))
            return jsonify({'status': 'QR code login successful'})
        return jsonify({'status': 'Already logged in'})


@app.route('/wild', methods=['GET'])
def wildberries_search():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'query parameter is required'}), 400

    items = get_wildberries_items(query)
    return jsonify(items)


if __name__ == '__main__':
    app.run(debug=True)
