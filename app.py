from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
#======這裡是呼叫的檔案內容=====

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('PbW8YhaRhfmp0Nd5elBwx+zG3IZnZuImyiLaw/UZFTyELkFV94ErauAYO/Nb8ydURk+ERC4zJBfEXSMcs2HKRz4uG4soAO6Ll3aXpsKgYufBIMJ2WXTHS+KHSreMMZEtgBbd3o165/FVkxYclxrJpwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('39c91c5d891df00796befd95d2e012e6')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '抓樂霸' in msg:
        message = Toreba_Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif 'test' in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token,message)
    else:
        pass


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
