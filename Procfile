import os
from flask import Flask, request, jsonify, render_template_string
import requests

app = Flask(__name__)

TOKEN = "8690826652:AAEEjIT4WqXUKQgW6pKP6yPCD-ARZER9Abk"
CHAT_ID = "8690826652"

@app.route('/')
def home():
    return render_template_string('''
        <html>
        <head><title>لوحة تجربة البوت</title></head>
        <body style="font-family: Arial; text-align: center; margin-top: 50px; background-color: #f4f4f9;">
            <div style="background: white; padding: 30px; display: inline-block; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1);">
                <h2>نظام مراقبة واستقبال الـ Webhook جاهز</h2>
                <p>هذه واجهة تجريبية للعميل لمعاينة عمل البوت واستلام التنبيهات فوراً:</p>
                <form action="/test-alert" method="POST">
                    <button type="submit" style="padding: 12px 25px; font-size: 16px; background-color: #28a745; color: white; border: none; border-radius: 5px; cursor: pointer;">إرسال طلب وتنبيه تجريبي الآن</button>
                </form>
            </div>
        </body>
        </html>
    ''')

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    send_telegram_alert("⚠️ تنبيه: تم استلام بيانات جديدة بنجاح عبر النظام!")
    return jsonify({"status": "success", "data": data}), 200

@app.route('/test-alert', methods=['POST'])
def test_alert():
    send_telegram_alert("✅ تجربة ناجحة: تم محاكاة طلب الزبون وإرسال التنبيه الفوري بنجاح!")
    return '''
        <h3 style="color: green; text-align: center; margin-top: 50px;">تم إرسال الطلب والتنبيه إلى تليجرام بنجاح! تحقق من هاتفك.</h3>
        <div style="text-align: center;"><a href="/" style="font-size: 18px;">العودة للخلف</a></div>
    '''

def send_telegram_alert(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}"
    try:
        requests.get(url)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
