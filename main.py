import requests
import time
from keep_alive import keep_alive

TOKEN = "7965663112:AAEwtPTPLE-sz-XC8RRXUBQs5AP1UYoifus"
URL = f"https://api.telegram.org/bot{TOKEN}"

def get_updates(offset=None):
    response = requests.get(URL + "/getUpdates", params={"offset": offset})
    return response.json()

def send_message(chat_id, text, button_url):
    reply_markup = {
        "inline_keyboard": [[
            {"text": "Open", "url": button_url}
        ]]
    }
    data = {
        "chat_id": chat_id,
        "text": text,
        "reply_markup": reply_markup
    }
    requests.post(URL + "/sendMessage", json=data)

def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if "result" in updates:
            for update in updates["result"]:
                message = update.get("message", {})
                text = message.get("text", "")
                chat_id = message["chat"]["id"]

                if text:
                    send_message(chat_id, "سلام! روی دکمه بزن:", "https://t.me/Sixp_robot/SIXP")

                last_update_id = update["update_id"] + 1
        time.sleep(2)

if __name__ == "__main__":
    keep_alive()
    main()
