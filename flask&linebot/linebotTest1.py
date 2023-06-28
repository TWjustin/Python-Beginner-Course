from flask import Flask
app = Flask(__name__)

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi('VIVvwvksXKlYrbhqJUikTbMc785mYrXn6SppaAvEC2OO3SR4rKlJlhsM59sTYGUeoioXrnwkcX+AhFdMCmtn0DRTZlgL30hudGaHFJWHfmmuksunktErbVczvl3hAvs8zm07uNTe3cdi9Y1bz1IeiwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5e7232804da455fa25ed8471e74a879b')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))

if __name__ == '__main__':
    app.run()