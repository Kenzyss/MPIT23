from flask import Flask, render_template, request
from flask_mail import Message, Mail
from chat import get_answer, start

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.rambler.ru'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'mpit23project@rambler.ru'  # адрес электронной почты
app.config['MAIL_PASSWORD'] = 'dFgHjK123'  # \ пароль

mail = Mail(app)

with app.app_context():
    recipient = "mpit23project@rambler.ru"
    subject = "hello"
    body = "Hello"
    lang = "rus"
    msg = Message(subject=subject,
                  recipients=["mpit23project@rambler.ru"], )
    msg.body = body
    # mail.send(msg)


@app.get("/")
def index_get():
    return render_template("base.html")


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    answer = get_answer(text)
    message = {"answer": answer}
    return message


start()
app.run(debug=True)
