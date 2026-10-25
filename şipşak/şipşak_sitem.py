from flask import Flask, render_template, jsonify
from flask_mail import Mail, Message

app = Flask(__name__, template_folder='html kodlarım', static_folder='css kodlarım', static_url_path='/static')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'senin.eposta.adresin@gmail.com' # Kendi adresini yaz
# DİKKAT: Buraya normal Gmail şifreni DEĞİL, Google hesabından alacağın 16 haneli "Uygulama Şifresi"ni girmelisin.
app.config['MAIL_PASSWORD'] = 'gmail_uygulama_sifresi_buraya' 
app.config['MAIL_DEFAULT_SENDER'] = 'senin.eposta.adresin@gmail.com' # Kendi adresini yaz

mail = Mail(app)

@app.route('/')
def ana_sayfa():
    return render_template('index.html')

@app.route('/pomodoro')
def pomodoro():
    return render_template('pomodoro.html')

@app.route('/hobiler')
def hobiler():
    # Burada senin ilgi alanlarını (çizim, örgü, dikiş, kitap okuma gibi) 
    # listeleyeceğimiz bir sayfa olacak.
    return render_template('hobiler.html')

@app.route('/notlar')
def notlar():
    return render_template('hızlı_notlar.html')

@app.route('/ajanda')
def ajanda():
    return render_template('ajanda.html')

@app.route('/hatirlatici')
def hatirlatici():
    return render_template('hatirlatici.html')

@app.route('/pomodoro_mail_gonder', methods=['POST'])
def pomodoro_mail_gonder():
    try:
        msg = Message(
            subject="🍅 Pomodoro Tamamlandı!",
            recipients=["cerenozer525@gmail.com"], # E-postanın kime gideceği
            body="Tebrikler Ceren! Odaklanma süren başarıyla bitti. Şimdi kahveni alıp biraz dinlenme vakti."
        )
        mail.send(msg)
        return jsonify({"durum": "basarili"}), 200
    except Exception as e:
        print("Mail gönderirken bir hata oluştu:", e)
        return jsonify({"durum": "hata", "mesaj": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 