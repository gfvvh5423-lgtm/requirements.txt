from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# إعدادات البوت والـ Chat ID المدمجة
BOT_TOKEN = "8690826652:AAEEjIT4WqXUKQgW6pKP6yPCD-ARZER9Abk"
CHAT_ID = "8690826652"

# إعدادات التحكم
CONFIG = {
    "target_price_threshold": 100
}

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, json=payload, timeout=5)
    except Exception as e:
        print(f"Error sending Telegram alert: {e}")

@app.route('/webhook', methods=['POST'])
def webhook_handler():
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "message": "Invalid payload"}), 400

    price = data.get('price', 0)
    
    if price < CONFIG['target_price_threshold']:
        msg = f"✅ Success: Condition met! Price is {price}."
        send_telegram_alert(msg)
        return jsonify({"status": "success", "price": price}), 200
    else:
        msg = f"⚠️ Info: Condition not met (Price: {price})."
        send_telegram_alert(msg)
        return jsonify({"status": "ignored", "price": price}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
