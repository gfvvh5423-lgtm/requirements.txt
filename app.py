from flask import Flask, request, jsonify, render_template_string
import requests

app = Flask(__name__)

# توكن البوت ومعرفك على تليجرام للتنبيهات
TOKEN = "8690826652:AAEEjIT4WqXUKQgW6pKP6yPCD-ARZER9Abk"
CHAT_ID = "8690826652" 

# 1. واجهة التجربة المرئية للزبون (تفتح عبر المتصفح مباشرة)
@app.route('/')
def home():
    return render_template_string('''
        <html>
        <head><title>تجربة بوت الـ Webhook</title></head>
        <body style="font-family: Arial; text-align: center; margin-top: 50px;">
            <h2>لوحة تجربة بوت الـ Webhook</h2>
            <p>اضغط على الزر أدناه لمحاكاة إرسال طلب جديد واختبار وصول التنبيه:</p>
            <form action="/test-order" method="POST">
                <button type="submit" style="padding: 15px 30px; font-size: 18px; background-color: #28a745; color: white; border: none; border-radius: 5px; cursor: pointer;">إرسال طلب تجريبي الآن</button>
            </form>
        </body>
        </html>
    ''')

# 2. مسار استقبال الـ Webhook الحقيقي من المصدر
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # هنا يتم معالجة البيانات وتحقق الشروط التي يريدها الزبون
    # مثال: إذا وصل طلب جديد، يتم إرسال إشعار تليجرام تلقائياً
    send_telegram_alert("⚠️ تنبيه: تم استلام بيانات جديدة عبر الـ Webhook بنجاح!")
    return jsonify({"status": "success", "received_data": data}), 200

# 3. مسار محاكاة التجربة للزبون عند الضغط على الزر في الصفحة
@app.route('/test-order', methods=['POST'])
def test_order():
    # محاكاة إرسال إشعار تجريبي للتاجر أو الزبون
    send_telegram_alert("✅ تجربة ناجح: تم محاكاة طلب شراء وتحقق الشروط بنجاح!")
    return "<h3>تم إرسال الطلب والتنبيه بنجاح! تحقق من تليجرام الخاص بك.</h3><a href='/'>العودة</a>"

def send_telegram_alert(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}"
    try:
        requests.get(url)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
